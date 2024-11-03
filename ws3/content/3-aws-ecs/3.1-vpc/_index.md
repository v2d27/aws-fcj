---
title : "VPC for ECS"
date : "`r Sys.Date()`"
weight : 1
chapter : false
pre : " <b> 3.1 </b> "
---

We create the network for ECS, runing on two availability zones. Each of AZ contains 01 public subnet and 01 private subnet. Also enable NAT gateway for private subnet.

Creating `ECS-main.tf` file with the configurations below (this file is also used in 3.2, 3.3 and 3.4 steps):

```terraform
locals {
    project_name = "webapp"
    region = data.aws_region.current.name
        
    vpc_cidr = "10.11.0.0/16"
    azs = slice(data.aws_availability_zones.available.names, 0, 2) # for [AZ]a and [AZ]b
}


module "vpc" {
    source = "terraform-aws-modules/vpc/aws"
    version = "~> 5.0"

    name = local.project_name
    cidr = local.vpc_cidr

    azs = local.azs
    private_subnets = [for k, v in local.azs : cidrsubnet(local.vpc_cidr, 8, k + 10)]
    public_subnets = [for k, v in local.azs : cidrsubnet(local.vpc_cidr, 8, k)] 

    
    # For static website, private subnets don't need to connect to the internet
    # enable_nat_gateway = false

    # if you want the container connect to internet
    enable_nat_gateway = true
    single_nat_gateway = true
}
```

For NAT gateway in this workshop, we are only create one NAT gateway which is used by two AZs. We should create each NAT gateway per availability zone (AZ) when deploying in product environment. Below are three options for you:

```terraform
# One NAT Gateway per subnet (default behavior)
enable_nat_gateway = true
single_nat_gateway = false
one_nat_gateway_per_az = false

# Single NAT Gateway
enable_nat_gateway = true
single_nat_gateway = true
one_nat_gateway_per_az = false

# One NAT Gateway per availability zone
enable_nat_gateway = true
single_nat_gateway = false
one_nat_gateway_per_az = true
```
About vpc module in Terraform registry: [AWS VPC Terraform module](https://registry.terraform.io/modules/terraform-aws-modules/vpc/aws/latest)