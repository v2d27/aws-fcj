---
title : "CloudServer Configuration"
date : "`r Sys.Date()`"
weight : 2
chapter : false
pre : " <b> 2. </b> "
---

#### Setup server can connect to internet through NAT gateway
In this step, we will need to create a VPC with one public and one private subnets. Then create an EC2 Instance Ubuntu located in the private subnet, a NAT gateway located in the public subnet
and creating Route Table for VPC.

The architecture overview after we complete this step will be as follows:

![cloud](/aws-fcj/ws1/images/2.cloudserver/cloud-01.png)

#### Table of Contents
1. [Create VPC](/2-CloudServer/2.1-createvpc)
2. [Create Subnet](/2-CloudServer/2.2-createsubnet)
3. [Create Security Group](/2-CloudServer/2.3-securitygroup)
4. [Create Internet Gateway](/2-CloudServer/2.4-createigw)
5. [Create NAT Gateway](/2-CloudServer/2.5-createnatgw)
6. [Create Routing Table](/2-CloudServer/2.6-routingtable)
7. [Create EC2 Server](/2-CloudServer/2.7-createec2)