---
title : "Other Resources"
date : "`r Sys.Date()`"
weight : 4
chapter : false
pre : " <b> 4.4 </b> "
---


```terraform
################################################################################
# ECR
################################################################################
resource "aws_ecr_repository" "web_app_ecr" {
    name = "${local.project_name}-frontend"

    # Allow to change image tag
    image_tag_mutability = "MUTABLE"
    
    # Disable scan images for software vulnerabilities
    image_scanning_configuration {
        scan_on_push = false
    }

    # Delete the repository even if it contains images
    force_delete = true
}
```

```terraform
################################################################################
# Cloudwatch log for ECS Container
################################################################################

resource "aws_cloudwatch_log_stream" "web_app_logs_stream" {
    name = "webapp_container_logs"
    log_group_name = aws_cloudwatch_log_group.webapp_logs.name
}

################################################################################
# Output
################################################################################
output "alb_hostname" {
    value = "${aws_alb.web_app_alb.dns_name}:${local.host_port}"
}
```

```terraform
################################################################
# Create S3 bucket to store Artifact
################################################################
resource "aws_s3_bucket" "webapp_s3bucket" {
    bucket = "${local.github_repository}-bucket-1001"
    force_destroy = true
}

# Create logs folder in S3 bucket
resource "aws_s3_object" "artifacts" {
    bucket = aws_s3_bucket.webapp_s3bucket.id
    force_destroy = true
    key = "artifacts/"
    acl = "private"
}
```

```terraform
################################################################
# CloudWatch
################################################################
resource "aws_cloudwatch_log_group" "webapp_logs" {
    name = "webapp_logs"
    # Retention 1 days
    retention_in_days = 1               
}

# Create a CloudWatch Log Stream within the Log Group
resource "aws_cloudwatch_log_stream" "codebuild_log" {
    name = "codebuild_log"
    log_group_name = aws_cloudwatch_log_group.webapp_logs.name
}
```