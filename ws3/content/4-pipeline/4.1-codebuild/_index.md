---
title : "AWS Code Build"
date : "`r Sys.Date()`"
weight : 1
chapter : false
pre : " <b> 4.1 </b> "
---


```terraform
################################################################
# IAM Role for CodeBuild
################################################################
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

################################################################
# Code Build
################################################################
locals {
    ecr_repository_url = aws_ecr_repository.web_app_ecr.repository_url
    github_repository = "aws-codepipeline"
    dockerhub_url = "hercules9/it_company_business:latest"
    account_id = data.aws_caller_identity.current.account_id
    shifttraffic_timeout = 120  # seconds (second must be equal to [minutes] * 60)
}

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

        # DockerHub variable
        # environment_variable {
        #     name = "DOCKER_USERNAME"
        #     value = var.dockerhub_account
        # }
        # environment_variable {
        #     name = "DOCKER_PASSWORD"
        #     value = var.dockerhub_password
        # }
        # environment_variable { 
        #     name = "IMAGE_NAME"
        #     value = local.dockerhub_url
        # }
        # environment_variable {
        #     name = "DOCKER_PATH"
        #     value = local.dockerhub_url
        # }

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

        # s3_logs {
        #     status = "ENABLED"
        #     location = "${aws_s3_bucket.aws_codepipeline.bucket}/buildlogs"
        # }
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

The `appspec.yaml` file is always called by CodeDeploy whenever it runs. Using `build-appspec.sh` file to pass arguments from Terraform to CodeDeploy through CodeBuild process. 

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


`Dockerfile`

- create docker image with all static website files inside nginx html 
- set container port to **port 80**

```Dockerfile
FROM nginx:alpine

COPY company-business /usr/share/nginx/html

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
```