---
title : "Init Environment"
date : "`r Sys.Date()`"
weight : 1
chapter : false
pre : " <b> 2.1 </b> "
---

We will set up necessary environmental variables for Terraform. With variable block, this is global variable that you can use it in anywhere in Terraform.

Terraform will load all files ***.tf** format in root module, so you can name the file whichever you want. Now, we will create `tf-variables.tf` file with all content in this page:

#### Init Terraform configuration

Specifying version to run. This workshop uses:
- Terraform version: `required_version = "1.9.6"`.
- Provider AWS: `hashicorp/aws version = "5.70.0"`.
- Template: `hashicorp/template = "2.2.0"`.

```terraform
terraform {
  required_providers {
    aws = {
      source = "hashicorp/aws"
      version = "5.70.0"
    }
    template = {
      source = "hashicorp/template"
      version = "2.2.0"
    }
  }
  required_version = "1.9.6"
}
```


#### Init Account
We have some security credentials in previous step. We need to load it into Terraform:

```terraform
# AWS Account
variable "access_key" {}
variable "secret_key" {}
```

#### Init Provider and Region
I choose the region Singapore. You can change it if you want:

```terraform
provider "aws" {
    secret_key = var.secret_key
    access_key = var.access_key
    region = "ap-southeast-1"  # Singapore
}
```

#### Init Data resources

Config data resources to get aws value when applying

```terraform
# Get current Account ID
data "aws_caller_identity" "current" {}

# Get current region
data "aws_region" "current" {}

# Get current availability zones of region
data "aws_availability_zones" "available" {}
```



Finally, we completely set up necessary variables and environment for Terraform. Please save it and go to next step.