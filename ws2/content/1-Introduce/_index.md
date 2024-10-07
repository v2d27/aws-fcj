---
title : "Introduction"
date :  "`r Sys.Date()`" 
weight : 1 
chapter : false
pre : " <b> 1. </b> "
---

#### VPC Limitation
Each AWS account can create a maximum of 5 Virtual Private Clouds (VPCs) in a single region by default. This limit is designed to help manage resources and ensure that users do not overwhelm the infrastructure. If your organization expands its activities, requires more environments with high availability and scalable flexibility, you will need to create cross-connections in many regions and accounts. This workshop will demonstrate two ways to facilitate communication between them in AWS.

![intro](/aws-fcj/ws2/images/ws2.png?width=1000)


#### VPC Peering

A VPC peering connection is a networking connection between two VPCs that enables you to route traffic between them using private IPv4 addresses or IPv6 addresses. Instances in either VPC can communicate with each other as if they are within the same network. You can create a VPC peering connection between your own VPCs, or with a VPC in another AWS account. The VPCs can be in different Regions (also known as an inter-Region VPC peering connection).
![intro](/aws-fcj/ws2/images/2.content/inter-region-vpc-peering.png)

#### Transit Gateway
A Transit Gateway functions as a virtual router, connecting multiple AWS VPCs and VPN connections within a single AWS account or across multiple accounts. It enables you to establish secure connections between your VPCs and on-premises networks, reducing the need for complex configurations and multiple connections. It provides third-party communication with other cloud providers.
![intro](/aws-fcj/ws2/images/2.content/tgw.png)


#### What are differents between Transit Gateway and VPC Peering?
You can see that we have two ways to make vpc connection. But they have some differences:

##### **1. For VPC Peering**
**- Connect VPCs within the Same AWS Region**: VPC Peering allows you to establish a one-to-one connection between two VPCs within the same AWS region, enabling communication between instances in each VPC using private IP addresses.

**- Inter-Region VPC Peering**: With VPC Peering, you can also connect VPCs across different AWS regions, allowing instances in each VPC to communicate with each other as if they were part of the same network.

##### **2. For Transit Gateway**

**- Connect Multiple VPCs and On-Premises Networks**: AWS Transit Gateway allows you to connect multiple VPCs and on-premises networks through a central hub, simplifying your network architecture and reducing the number of connections you need to manage.

**- Centralized Routing and Security Policies**: With AWS Transit Gateway, you can enforce and manage centralized routing and security policies across your entire network, making it easier to maintain consistent network-wide rules.

**- Support for Hybrid Cloud Environments**: AWS Transit Gateway natively supports connections to on-premises networks through VPN connections or AWS Direct Connect, making it a suitable solution for hybrid cloud environments.

**- Inter-Region Connectivity**: AWS Transit Gateway supports inter-region peering, allowing you to connect VPCs across different AWS regions and improve network performance and resiliency.



#### Terraform

![intro](/aws-fcj/ws2/images/2.content/terraform.png)

Terraform is an open-source tool developed by HashiCorp for Infrastructure as Code (IaC), which enables users to define and manage cloud infrastructure through code rather than manual setup or point-and-click interfaces. Terraform shortens construction time and supports complex multi-region architecture, so it helps me optimizing my costs when using AWS services.







#### AWS services
**- VPN Site-to-Site**: Securely connects on-premises networks to AWS VPCs over an encrypted tunnel, extending your network into the cloud.

**- Transit Gateway**: Central hub that connects multiple VPCs and on-premises networks, simplifying network management across regions and accounts.

**- VPC Peering**: Direct, private connection between two VPCs, allowing seamless communication without the public internet.

**- Session Manager**: Provides secure, browser-based shell access to EC2 instances, eliminating the need for SSH and public IPs. 

**- IAM Roles**: Grant temporary access to AWS S3 resource securely for users and services, managed through policies.

**- Amazon S3**: Scale storage for Session Manager logs.





#### Estimate Costs

For more infomation and to understand how AWS caculates, please visit the following pages:
+ [AWS VPN Site-to-Site Pricing](https://aws.amazon.com/vpn/pricing/)
+ [Transit Gateway Pricing](https://aws.amazon.com/transit-gateway/pricing/)
+ [VPC Peering Pricing](https://aws.amazon.com/about-aws/whats-new/2021/05/amazon-vpc-announces-pricing-change-for-vpc-peering/)

To complete this workshop you will spend about **0.5$ each hour** for free-tier accounts.
