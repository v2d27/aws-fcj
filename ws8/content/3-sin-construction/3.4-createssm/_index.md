---
title : "Create Session Manager"
date : "`r Sys.Date()`"
weight : 4
chapter : false
pre : " <b> 3.4 </b> "
---


#### IAM Role

Creating `sin-iam.tf` file with the configurations below:


```terraform
# Create the IAM Role for EC2
resource "aws_iam_role" "SessionManager-Role" {
    provider = aws.region_singapore
    name = "SessionManager-Role"

    assume_role_policy = jsonencode({
        Version = "2012-10-17"
        Statement = [
            {
                Action = "sts:AssumeRole"
                Effect = "Allow"
                Principal = {
                Service = "ec2.amazonaws.com"
                }
            }
        ]
    })
}

# Attach the AmazonSSMManagedInstanceCore
resource "aws_iam_role_policy_attachment" "AmazonSSMManagedInstanceCore" {
    provider = aws.region_singapore
    role = aws_iam_role.SessionManager-Role.name
    policy_arn = "arn:aws:iam::aws:policy/AmazonSSMManagedInstanceCore"
}

# Attach the AmazonS3FullAccess
resource "aws_iam_role_policy_attachment" "AmazonS3FullAccess" {
    provider = aws.region_singapore
    role = aws_iam_role.SessionManager-Role.name
    policy_arn = "arn:aws:iam::aws:policy/AmazonS3FullAccess"
}


# Create IAM profile to attach EC2
resource "aws_iam_instance_profile" "SessionManager-Profile" {
    provider = aws.region_singapore
    name = "SessionManager-Profile"
    role = aws_iam_role.SessionManager-Role.name
}

```

#### AWS S3 Bucket

Creating `sin-s3.tf` file with the configurations below:

```terraform
# Create S3 bucket 
resource "aws_s3_bucket" "ssm-bucket-0001" {
    provider = aws.region_singapore
    bucket = "ssm-bucket-0001"
    force_destroy = true # To allow Terraform to delete non-empty buckets
    tags = {
        Name = "ssm-bucket-0001"
    }
} # => Default s3 ACL is private

# Create logs folder in S3 bucket
resource "aws_s3_object" "logs" {
    provider = aws.region_singapore
    bucket = aws_s3_bucket.ssm-bucket-0001.id
    force_destroy = true
    key = "logs/"
    acl = "private"
}

```