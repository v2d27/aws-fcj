---
title : "Initialization Providers"
date : "`r Sys.Date()`"
weight : 2
chapter : false
pre : " <b> 2.2 </b> "
---


We will create `tf-provider.tf` file with all content in this page:

I will choose region **Singapore** in account 1 and region **Virginia** (US) in account 2:


```terraform
###########################################################################################################
# I will use "alias" in both two accounts to easily distinguish
# Settings bellow will set default provider for terraform, so you won't be worry about missing "provider"
#
# provider "aws" {
#     access_key = var.access_key_1
#     secret_key = var.secret_key_1
#     region = var.region_singapore
# }
###########################################################################################################

# Account 1, Region: Singapore
provider "aws" {
    access_key = var.access_key_1
    secret_key = var.secret_key_1
    region = var.region_singapore
    alias = "region_singapore"
}

# Account 2, Region: Virginia
provider "aws" {
    access_key = var.access_key_2
    secret_key = var.secret_key_2
    region = var.region_virginia
    alias = "region_virginia"
}
```

We also need the target account ID to establish inter-region connection, so we can use caller to get target AWS AccountID. In this workshop, target or accepter account is US region.


```terraform
# use caller to get target AWS AccountID
data "aws_caller_identity" "target" {
    provider = aws.region_virginia
}
```

