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
            "logs:PutLogEvents"
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