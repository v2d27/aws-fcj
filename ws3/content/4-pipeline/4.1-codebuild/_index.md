---
title : "AWS Code Build"
date : "`r Sys.Date()`"
weight : 1
chapter : false
pre : " <b> 4.1 </b> "
---

There are some following contents in this step:
- [1. Terraform infrastructure](#1-terraform-infrastructure)
- [2. CodeBuild pipeline file](#2-codebuild-pipeline-file)
- [3. Making CodeDeploy file ](#3-making-codedeploy-file)
- [4. Making image by Dockerfile](#4-making-image-by-dockerfile)

### 1. Terraform infrastructure

#### IAM Role for CodeBuild

```terraform
resource "aws_iam_role" "codebuild_role" {
    name = "CodeBuildServiceRole"
    assume_role_policy = file("./templates/policies/codebuild_role.json")
}

resource "aws_iam_policy" "codebuild_policy" {
    name = "CodeBuildPolicy"
    description = "Policy for CodeBuild to access S3, CloudWatch, and GitHub."
    policy = file("./templates/policies/codebuild_policy.json")
}

resource "aws_iam_role_policy_attachment" "codebuild_attachment" {
    role = aws_iam_role.codebuild_role.name
    policy_arn = aws_iam_policy.codebuild_policy.arn
}
```

#### Variables

```terraform
locals {
    # URL of the ECR repository where Docker images are stored
    ecr_repository_url = aws_ecr_repository.web_app_ecr.repository_url
    
    # Name of the GitHub repository used in the pipeline
    github_repository = "aws-codepipeline"
    
    # AWS account ID of the current caller
    account_id = data.aws_caller_identity.current.account_id
    
    # Timeout duration for traffic shifting during deployment, specified in seconds
    shifttraffic_timeout = 120  # seconds (seconds must be equal to [minutes] * 60)
}

```

#### Code Build

Define an AWS CodeBuild project integrated with AWS CodePipeline for automated builds. It contains essential properties such as the IAM role, build timeout, and environment settings, including the Docker image and compute type. Key environment variables are defined to manage deployment configurations and logging to CloudWatch is set up for tracking build activities. The project sources its code from CodePipeline, using a specified `buildspec.yaml` file to guide the build process. More at Terraform registry: [aws_codebuild_project](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/codebuild_project).

```terraform
resource "aws_codebuild_project" "aws_codepipeline" {
    name = "aws_codepipeline"
    description = "aws_codepipeline"
    build_timeout = 5
    service_role = aws_iam_role.codebuild_role.arn

    artifacts {
        type = "CODEPIPELINE"
    }

    environment {
        compute_type = "BUILD_GENERAL1_MEDIUM"
        image = "aws/codebuild/standard:7.0" # for image standard:7.0 = > must run on BUILD_GENERAL1_MEDIUM
        type = "LINUX_CONTAINER"
        image_pull_credentials_type = "CODEBUILD"

        # ECR variable
        environment_variable {
            name = "IMAGE_NAME"
            value = local.ecr_repository_url
        }

        environment_variable {
            name = "AWS_REGION"
            value = data.aws_region.current.name
        }

        environment_variable {
            name = "AWS_ACCOUNT_ID"
            value = local.account_id
        }

        # CodeDeploy for appspec.yaml file
        environment_variable {
            name = "TASK_DEFINITION"
            value = aws_ecs_task_definition.web_app_task.arn
        }

        environment_variable {
            name = "CONTAINER_NAME"
            value = local.container_name
        }

        environment_variable {
            name = "CONTAINER_PORT"
            value = local.container_port
        }

        environment_variable {
            name = "SHIFTTRAFFIC_TIMEOUT"
            value = local.shifttraffic_timeout
        }
    }

    logs_config {
        cloudwatch_logs {
            group_name = aws_cloudwatch_log_group.webapp_logs.name
            stream_name = aws_cloudwatch_log_stream.codebuild_log.name
        }
    }

    # build directly from github ----------------------------------------------------------
        # source {
        #     type = "GITHUB"
        #     location = "https://github.com/v2d27/aws-codepipeline.git"
        #     git_clone_depth = 1
        # }
        # # github branch
        # source_version = "main"
    # -------------------------------------------------------------------------------------

    # build from AWS CodePipeline ---------------------------------------------------------
    source {
        type = "CODEPIPELINE"
        buildspec = "buildspec.yaml"
    }
    # -------------------------------------------------------------------------------------
}
```


### 2. CodeBuild pipeline file

Declare the `buildspec.yaml` file:

- **pre_build:**
    - Get authentications and Log in AWS ECR through AWS-CLI.
    - Calculating image uri base on the hash of repository and time when building started. Source of image path come from Terraform environment.
    - Note: the linux container **aws/codebuild/standard:7.0 (Ubuntu 22.04)** has available `docker` and `aws-cli` packages. Too see what programs are inside, please go to this GitHub project:  [aws-codebuild-docker-images/ubuntu/standard/7.0/Dockerfile](https://github.com/aws/aws-codebuild-docker-images/blob/master/ubuntu/standard/7.0/Dockerfile).
- **build:**
    - Build Docker image with lastest tag and current tag.

- **post_build:**
    - Build appspec.yaml file, used by CodeDeploy.
    - Export this file to CloudWatch to easily debug later.

- **artifacts**:
    - Upload appspec.yaml file to CodePipeline artifact, so CodeDeploy can read it.

```yaml
version: 0.2

phases:
  pre_build:
    commands:
      - echo Logging in AWS ECR
      - aws ecr get-login-password --region $AWS_REGION | docker login --username AWS --password-stdin $AWS_ACCOUNT_ID.dkr.ecr.$AWS_REGION.amazonaws.com

      - echo Calculating image uri
      - TAG="$(echo $CODEBUILD_RESOLVED_SOURCE_VERSION | cut -c1-8)_$(date +"%Y%m%d_%H%M%S")"

      - export IMAGE="${IMAGE_NAME}:$TAG"
      - export IMAGE_LATEST="${IMAGE_NAME}:latest"

      - echo -e "IMAGE=${IMAGE}\nIMAGE_LATEST=${IMAGE_LATEST}" > image_uri.txt
      - cat image_uri.txt

  build:
    commands:
      - echo "Building docker image"
      - docker build -f Dockerfile -t $IMAGE .
      - docker tag $IMAGE $IMAGE_LATEST

      - echo "Push $IMAGE to ECR"
      - docker push $IMAGE

      - echo "Push $IMAGE_LATEST to AWS ECR"
      - docker push $IMAGE_LATEST
  post_build:
    commands:
      - echo Logging out ECR
      - docker logout

      - echo Update appspec.yaml file 
      - bash build-appspec.sh $TASK_DEFINITION $CONTAINER_NAME $CONTAINER_PORT $SHIFTTRAFFIC_TIMEOUT

artifacts:
  base-directory: .
  files:
    - appspec.yaml

```


### 3. Making CodeDeploy file 

The *appspec.yaml* file is always called by CodeDeploy whenever it runs. Using *build-appspec.sh* file to pass arguments from Terraform to CodeDeploy through CodeBuild process. 

Declare the `build-appspec.sh` file:

```bash
#!/bin/bash

#################################################################
# This file called by buildspec.yaml
#################################################################

TASK_DEFINITION=$1
CONTAINER_NAME=$2
CONTAINER_PORT=$3
SHIFTTRAFFIC_TIMEOUT=$4
APPSPEC_FILE="appspec.yaml"


echo "version: 0.0
Resources:
  - TargetService:
      Type: AWS::ECS::Service
      Properties:
        TaskDefinition: \"${TASK_DEFINITION}\"
        LoadBalancerInfo:
          ContainerName: \"${CONTAINER_NAME}\"
          ContainerPort: ${CONTAINER_PORT}
        PlatformVersion: \"LATEST\"" > $APPSPEC_FILE

echo "Updating ${APPSPEC_FILE} content-----------------------------------"
cat $APPSPEC_FILE
echo "-----------------------------------------------------------------"
```


### 4. Making image by Dockerfile

- create docker image with all static website files inside nginx html 
- set container port to **port 80**
- install stress test package to increase CPU usage, used for validating AutoScaling

Declare the `Dockerfile` file:

```Dockerfile
FROM nginx:alpine

# RUN apk update && apk add --no-cache stress-ng
RUN apk add --no-cache stress-ng

# Example: increase cpu usage to 100% in 120s
# => docker exec -it [container_name] stress-ng --cpu 0 --timeout 120s

COPY company-business /usr/share/nginx/html

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]

```