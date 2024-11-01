---
title : "Create Instances"
date : "`r Sys.Date()`"
weight : 3
chapter : false
pre : " <b> 3.3 </b> "
---

Creating `sin-instances.tf` file with the configurations below:

```terraform

# Create EC2 for VPC1
resource "aws_instance" "vpc1_instance" {
    provider = aws.region_singapore
    ami = "ami-0aa097a5c0d31430a"  # Amazon Linux AMI 2023
    instance_type = "t2.micro"
    subnet_id = aws_subnet.VPC1-Subnet-Public.id
    security_groups = [aws_security_group.VPC1-SG-Public.id]
    associate_public_ip_address = true
    key_name = "aws-lab"

    tags = {
        Name = "vpc1_instance"
    }
}

# Create EC2 for VPC2
resource "aws_instance" "vpc2_instance" {
    provider = aws.region_singapore
    ami = "ami-0aa097a5c0d31430a"  # Amazon Linux AMI 2023
    instance_type = "t2.micro"
    subnet_id = aws_subnet.VPC2-Subnet-Private.id
    security_groups = [aws_security_group.VPC2-SG-Private.id]
    associate_public_ip_address = false
    key_name = "aws-lab"

    iam_instance_profile = aws_iam_instance_profile.SessionManager-Profile.name

    tags = {
        Name = "vpc2_instance"
    }
}


# Create EC2 for VPC3
resource "aws_instance" "vpc3_instance" {
    provider = aws.region_singapore
    ami = "ami-0aa097a5c0d31430a"  # Amazon Linux AMI 2023
    instance_type = "t2.micro"
    subnet_id = aws_subnet.VPC3-Subnet-Public.id
    security_groups = [aws_security_group.VPC3-SG-Public.id]
    associate_public_ip_address = true
    key_name = "aws-lab"
    
    tags = {
        Name = "vpc3_instance"
    }
}
```

#### Create SSH keypair

If you have already key_name in AWS cloud, you simply enter key name as I did above. 

In case you don't have any key, you have two ways to create it:
1. You can follow these steps [AWS Create Key Pair](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/create-key-pairs.html) to create key pair on AWS cloud and enter your **key_name**.

2. Using ssh-keygen to create a key pair and name it EC2. Run this command to create:
```bash
ssh-keygen -b 2048 -t rsa
```

Import key to Terraform (example):



```terraform
# example aws_instance
resource "aws_instance" "vpc3_instance" {
   ...
   key_name = aws_key_pair.aws-lab
   ...
}

# Import key pair from file
resource "aws_key_pair" "aws-lab" {
   provider = aws.region_singapore
   key_name = "aws-lab"
   public_key = file("../../aws-lab.pub") # put your public key here
}

```

{{%notice note%}}
If you create key pair from AWS website interface, this key is only available for current region. In other regions, please create the new one to access your EC2.
{{%/notice%}}