---
title : "N.Virginia Construction"
date :  "`r Sys.Date()`" 
weight : 4
chapter : false
pre : " <b> 4. </b> "
---


**N.Virginia region**: The second account will use one Region in **us-east-1**. We will create two VPCs inside with private subnet. All of them can not connect to internet. VPC5 will help us validating **VPN connection** and **Transit Gateway** peering connection. VPC4 will help us validating the **Inter-region VPC Peering** connection.

**On-premise region**: This is simulation of on-premise server, which is using **LibreSwan** instead of my real devices for establishing VPN Site-to-Site connection to AWS Cloud. It contains a Internet Gateway, a VPC and a EC2 with public subnet inside. We will automate the installation processing LibreSwan by Bashshell through Terraform. You can understand more about [LibreSwan here](https://v2d27.github.io/aws-fcj/ws1/4-sitetositevpn/4.4-libreswan/).

![intro](/aws-fcj/ws2/images/2.content/us.png)

Now, let start contruct!

#### Contents
- [4.1 Create Networks](/4-us-construction/4.1-createnetwork)
- [4.2 Create Security Groups](/4-us-construction/4.2-createsecurity)
- [4.3 Create Instances](/4-us-construction/4.3-createinstance)
- [4.4 Create Trasit Gateway](/4-us-construction/4.4-createtransit)