---
title : "AWS Code Pipeline"
date : "`r Sys.Date()`"
weight : 3
chapter : false
pre : " <b> 4.3 </b> "
---

```terraform
################################################################
# IAM Role for Code Pipeline
################################################################
resource "aws_iam_role" "codepipeline_role" {
    name = "codepipeline_role"
    assume_role_policy = file("./templates/policies/codepipeline_role.json")
}

resource "aws_iam_role_policy" "codepipeline_policy" {
    name = "codepipeline_policy"
    role = aws_iam_role.codepipeline_role.id
    policy = file("./templates/policies/codepipeline_policy.json")
}

resource "aws_iam_role_policy_attachment" "codepipeline_attachment" {
    role = aws_iam_role.codepipeline_role.name
    policy_arn = aws_iam_policy.codebuild_policy.arn
}

################################################################
# Code Pipeline
################################################################
# Data source to retrieve the GitHub OAuth token from Secrets Manager
data "aws_secretsmanager_secret" "github_personal_access_token" {
  name = "GitHub-v2d27"
}

data "aws_secretsmanager_secret_version" "github_personal_access_token" {
  secret_id = data.aws_secretsmanager_secret.github_personal_access_token.id
}

resource "aws_codestarconnections_connection" "v2d27_github_connection" {
    name = "v2d27-github-connection"
    provider_type = "GitHub"
    # Validate codestar connections manually since July 2024
}

resource "aws_codepipeline" "web_app_pipeline" {
    name = "${local.project_name}_pipeline"
    role_arn = aws_iam_role.codepipeline_role.arn

    artifact_store {
        location = aws_s3_bucket.webapp_s3bucket.bucket
        type = "S3"
    }

    stage {
        name = "Source"
        action {
            name = "SourceAction"
            category = "Source"
            owner = "AWS"
            provider = "CodeStarSourceConnection"
            version = "1"
            output_artifacts = ["source-output"]

            configuration = {
                ConnectionArn = aws_codestarconnections_connection.v2d27_github_connection.arn
                FullRepositoryId = "v2d27/aws-codepipeline"
                BranchName = "main"
            }
        }
    }

    stage {
        name = "Build"
        action {
            name = "BuildAction"
            category = "Build"
            owner = "AWS"
            provider = "CodeBuild"
            version = "1"
            input_artifacts = ["source-output"]
            output_artifacts = ["build-output"]
            configuration = {
                ProjectName = aws_codebuild_project.aws_codepipeline.name
            }
        }
    }

    stage {
        name = "Deploy"
        action {
            name = "DeployAction"
            category = "Deploy"
            owner = "AWS"
            provider = "CodeDeploy"
            version = "1"
            input_artifacts = ["build-output"]
            configuration = {
                ApplicationName = aws_codedeploy_app.webapp_codedeploy.name
                DeploymentGroupName = aws_codedeploy_deployment_group.webapp_deploygroup.deployment_group_name
            }
        }
    }
}

output "codepipeline_name" {
    value = aws_codepipeline.web_app_pipeline.name
}

output "ecr_repository_url" {
    value = aws_ecr_repository.web_app_ecr.repository_url
}
```