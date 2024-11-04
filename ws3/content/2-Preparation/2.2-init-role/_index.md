---
title : "Init IAM Roles and Policies"
date : "`r Sys.Date()`"
weight : 2
chapter : false
pre : " <b> 2.2 </b> "
---

We config services roles and policies through json files, making roles and policies management more easily. Below is a list of services to be configured:

- [ECS Task Roles and Policies](#ecs-task-roles-and-policies)
- [CodeBuild Roles and Policies](#ecs-task-roles-and-policies)
- [CodeDeploy Roles and Policies](#codedeploy-roles-and-policies)
- [CodePipeline Roles and Policies](#codepipeline-roles-and-policies)
- [AutoScaling Roles](#autoscaling-roles)

#### ECS Task Roles and Policies

- **Json Roles path**: `templates\policies\ecstask_role.json`

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
        "Action": "sts:AssumeRole",
        "Principal": {
            "Service": "ecs-tasks.amazonaws.com"
        },
        "Effect": "Allow",
        "Sid": ""
        }
    ]
}
```

- **Json Policies path**: `templates\policies\ecstask_policy.json`
- Allow Pulling docker image from AWS ECR.
- Allow exporting container logs to CloudWatch Logs.
- Allow SSM and SSMMESSAGES policy to interact with AWS-CLI.
- Allow to access all ECS cluster.
- **Note**: *We have **task_role_arn** and **execution_role_arn** use this IAM Roles. We should split into two seperated roles. In this workshop, both of ECS Task and Container will run the same role for testing. Please check this resource in Terraform: **aws_ecs_task_definition.web_app_task***

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
        "Effect": "Allow",
        "Action": [
            "ecr:*",
            "logs:CreateLogGroup",
            "logs:CreateLogStream",
            "logs:PutLogEvents",
            "ssmmessages:*",
            "ssm:*",
            "ecs:*"
        ],
        "Resource": "*"
        }
    ]
}
```


#### CodeBuild Roles and Policies

- **Json Roles path**: `templates\policies\codebuild_role.json`

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
        "Effect": "Allow",
        "Principal": {
            "Service": "codebuild.amazonaws.com"
        },
        "Action": "sts:AssumeRole"
        }
    ]
}
```

- **Json Policies path**: `templates\policies\codebuild_policy.json`

- Grant AWS CodeBuild the necessary permissions to access S3, CloudWatch Logs, CodeBuild, Secrets Manager, ECR, and ECS for essential build and deployment tasks: 
  - CodeBuild can retrieve, store, and list objects in S3, allowing it to manage source code and build artifacts. 
  - It can also create and write logs in CloudWatch Logs, enabling detailed logging of build activities. 
  - Within CodeBuild itself, it can start, update, and stop builds as well as retrieve information on past builds. 
  - Access to Secrets Manager allows CodeBuild to securely retrieve sensitive information, while permissions for ECR provide full control over container images used in builds. 
  - ECS permissions allow CodeBuild to describe and update ECS services and clusters, enabling automated deployments and updates to containerized applications.


```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
        "Effect": "Allow",
        "Action": [
            "s3:GetObject",
            "s3:PutObject",
            "s3:ListBucket",
            "logs:CreateLogGroup",
            "logs:CreateLogStream",
            "logs:PutLogEvents",
            "codebuild:BatchGetBuilds",
            "codebuild:StartBuild",
            "codebuild:UpdateProject",
            "codebuild:StopBuild",
            "secretsmanager:GetSecretValue",
            "ecr:*",
            "ecs:DescribeCluster",
            "ecs:DescribeServices",
            "ecs:UpdateService"
        ],
        "Resource": "*"
        }
    ]
}
```

#### CodeDeploy Roles and Policies

- **Json Roles path**: `templates\policies\codedeploy_role.json`

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
        "Effect": "Allow",
        "Principal": {
            "Service": "codedeploy.amazonaws.com"
        },
        "Action": "sts:AssumeRole"
        }
    ]
}
```

- **Json Policies path**: `templates\policies\codedeploy_policy.json`

- AWS CodeDeploy with the necessary permissions to manage ECS deployments, access logging and monitoring services, and interact with S3 and Elastic Load Balancing: 
  - CodeDeploy can describe and update ECS clusters, services, and task definitions, as well as create and manage task sets, allowing it to control the deployment process and handle blue/green deployment workflows in ECS. 
  - The iam:PassRole permission enables CodeDeploy to use specified IAM roles during deployment. 
  - Logging permissions in CloudWatch Logs allow for creating log groups and streams and writing log data, which aids in tracking deployment activities. 
  - Additionally, the policy allows CodeDeploy to send custom metrics to CloudWatch and interact with S3 for storing and retrieving deployment files. 
  - Full Elastic Load Balancing permissions enable CodeDeploy to manage load balancer settings, ensuring smooth traffic routing during deployments. 
  - This comprehensive set of permissions supports automated and controlled deployment operations.


```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
        "Effect": "Allow",
        "Action": [
            "ecs:DescribeClusters",
            "ecs:DescribeServices",
            "ecs:DescribeTaskDefinition",
            "ecs:UpdateService",
            "ecs:ListTasks",
            "ecs:DescribeTasks",
            "ecs:CreateTaskSet",
            "ecs:DeleteTaskSet",
            "ecs:UpdateServicePrimaryTaskSet",
            "iam:PassRole",
            "logs:CreateLogGroup",
            "logs:CreateLogStream",
            "logs:PutLogEvents",
            "cloudwatch:PutMetricData",
            "s3:GetObject",
            "s3:PutObject",
            "s3:ListBucket",
            "elasticloadbalancing:*"
        ],
        "Resource": "*"
        }
    ]
}
```

#### CodePipeline Roles and Policies

- **Json Roles path**: `templates\policies\codepipeline_role.json`

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
        "Effect": "Allow",
        "Principal": {
            "Service": "codepipeline.amazonaws.com"
        },
        "Action": "sts:AssumeRole"
        }
    ]
}
```

- **Json Policies path**: `templates\policies\codepipeline_policy.json`

- AWS CodePipeline the permissions are needed for orchestrating and managing end-to-end CI/CD pipelines: 
  - With S3 permissions (GetObject, PutObject, ListBucket), CodePipeline can access source code, build artifacts, and deployment assets stored in S3. 
  - CloudWatch Logs permissions allow it to create log groups and streams and publish log events, enabling detailed logging and monitoring of pipeline actions. 
  - The ecs:UpdateService permission enables CodePipeline to update ECS services, essential for deploying new container images.
  - Permissions for CodeStar and CodeStar Connections allow CodePipeline to integrate with external GitHub repositories, while full permissions for CodeBuild and CodeDeploy (codebuild:*, codedeploy:*) enable it to initiate builds, manage deployment configurations, and control deployment workflows. 
  These permissions collectively allow CodePipeline to automate the stages of software delivery, including building, testing, deploying, and managing applications.

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
        "Effect": "Allow",
        "Action": [
            "s3:GetObject",
            "s3:PutObject",
            "s3:ListBucket",
            "logs:CreateLogGroup",
            "logs:CreateLogStream",
            "logs:PutLogEvents",
            "ecs:UpdateService",
            "codestar:*",
            "codestar-connections:*",
            "codebuild:*",
            "codedeploy:*"
        ],
        "Resource": "*"
        }
    ]
}
```

#### AutoScaling Roles

- **Json Roles path**: `templates\policies\app_autoscale_role.json`

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
        "Effect": "Allow",
        "Principal": {
            "Service": "application-autoscaling.amazonaws.com"
        },
        "Action": "sts:AssumeRole"
        }
    ]
}
```


Finally, we completely set up necessary variables and environment for Terraform. Please save it and go to next step.