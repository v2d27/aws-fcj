---
title : "Preparation"
date : "`r Sys.Date()`"
weight : 2
chapter : false
pre : " <b> 2. </b> "
---
Before you begin please ensure that: [**an active AWS account and AWS CLI configured**](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-quickstart.html) and [**Terraform installed**](https://developer.hashicorp.com/terraform/tutorials/aws-get-started/install-cli)

#### Accounts

You need to collect your [AWS IAM User](https://console.aws.amazon.com/iam/home#/users) **access_key** and **secret_key** of your account. After that, creating `terraform.tfvars` file in your projects and replacing your information:

```terraform
# terraform.tfvars default loading when applying 
# if you change its name, please add arguments -var-file="[new_name].tfvars"
 
# Enter your access_key and secret_key for account 1
access_key_1 = "[account_1_access_key]"
secret_key_1 = "[account_1_secret_key]"

# Enter your access_key and secret_key for account 2
access_key_2 = "[account_2_access_key]"
secret_key_2 = "[account_2_secret_key]"
```

AWS IAM (Identity and Access Management) user’s access key and secret access key are **displayed only once** when they are initially created. After that, you cannot retrieve the secret access key again through the AWS Management Console, AWS CLI, or any other method. If you lose it, you’ll need to delete the old access key and create a new one.

{{%notice note%}}
You can complete this workshop in one account by entering the same **access_key** and **secret_key** in "terraform.tfvars" file.
{{%/notice%}}

#### Regions
First region, **Singapore** region with region code: `ap-southeast-1` for Account 1.

Second region, **N. Virginia** (USA) region with region code: `us-east-1` for Account 2.


#### Workshop Structure
This structure represents where files are located and all these files work together in the root module to define and manage the infrastructure as code using Terraform.
```bash
My Workshop
├── .gitignore
├── sin-iam.tf
├── sin-instances.tf
├── sin-network.tf
├── sin-s3.tf
├── sin-security.tf
├── sin-transit.tf
├── terraform.tfvars
├── tf-output.tf
├── tf-provider.tf
├── tf-variables.tf
├── transit-peering.tf
├── transit-vpn.tf
├── us-instances.tf
├── us-network.tf
├── us-security.tf
├── us-transit.tf
└── vpc-peering.tf
```


{{%notice warning%}}
**terraform.tfvars** file contains security credentials. Please prevent it from uploading your secret infomation by adding ***.tfvars** line in `.gitignore` if you are using git.
{{%/notice%}}