---
title : "Review Configurations"
date : "`r Sys.Date()`"
weight : 2
chapter : false
pre : " <b> 8.2 </b> "
---

{{% notice tip %}}
***This is optional step, please skip it and go to [clean up resources](/9-cleanup).***
{{% /notice %}}

#### I. Singapore region
VPC1, VPC2, VPC3 state in Singapore region is **Available**

![intro](/aws-fcj/ws2/images/3.validating/vpc123_state.png)

All subnet of VPC1, VPC2, VPC3 state in Singapore region is **Available**

![intro](/aws-fcj/ws2/images/3.validating/vpc123_subnet.png)


Route table of VPC1:
- VPC1 can connect to Internet through Internet Gateway.
- VPC1 can connect to all VPC in 10.0.0.0/8 range through Transit Gateway.
- VPC1 can connect to on-premise server 192.168.0.0/16 through Transit Gateway.

![intro](/aws-fcj/ws2/images/3.validating/vpc1_rt.png)

Route table of VPC2:
- VPC2 can connect to AWS S3 Bucket through VPC endpoint Gateway (the target is prefix list of AWS S3 Bucket).
- VPC2 can connect to all VPC in 10.0.0.0/8 range through Transit Gateway.
- VPC2 can connect to on-premise server 192.168.0.0/16 through Transit Gateway.

![intro](/aws-fcj/ws2/images/3.validating/vpc2_rt.png)


Internet Gateway for VPC1 and VPC3 in Singapore region

![intro](/aws-fcj/ws2/images/3.validating/igw.png)


Validating Security Group for VPC1

![intro](/aws-fcj/ws2/images/3.validating/sg_vpc1_in.png)

![intro](/aws-fcj/ws2/images/3.validating/sg_vpc1_out.png)

Validating Security Group for VPC2

![intro](/aws-fcj/ws2/images/3.validating/sg_vpc2_in.png)
![intro](/aws-fcj/ws2/images/3.validating/sg_vpc2_out.png)

Validating Security Group for VPC3

![intro](/aws-fcj/ws2/images/3.validating/sg_vpc3_in.png)
![intro](/aws-fcj/ws2/images/3.validating/sg_vpc3_out.png)

Validating Security Group for VPC2 Endpoint

![intro](/aws-fcj/ws2/images/3.validating/sg_vpc2_endpoint_out.png)
![intro](/aws-fcj/ws2/images/3.validating/sg_vpc2_endpoint.png)


**Validating Transit Gateway**

Transit Gateways

![intro](/aws-fcj/ws2/images/3.validating/tgw.png)

Transit Gateway Attachments

![intro](/aws-fcj/ws2/images/3.validating/tgw_peering.png)

Transit Gateway Route Table Associates

![intro](/aws-fcj/ws2/images/3.validating/tgw_rt_acc.png)

Transit Gateway Route Table Propagations

![intro](/aws-fcj/ws2/images/3.validating/tgw_rt_pro.png)


Transit Gateway Route Table

![intro](/aws-fcj/ws2/images/3.validating/tgw_rt.png)


**VPN Connection**

Customer Gateway

![intro](/aws-fcj/ws2/images/3.validating/cgw.png)

VPN Connection between VPN and Transit Gateway

![intro](/aws-fcj/ws2/images/3.validating/transit_vpn.png)



**IAM Role**

IAM role

![intro](/aws-fcj/ws2/images/3.validating/iam_role.png)

IAM role permission

![intro](/aws-fcj/ws2/images/3.validating/iam_role_permission.png)


**Endpoint**

VPC2 endpoint Gateway

![intro](/aws-fcj/ws2/images/3.validating/endpoint.png)

VPC2 endpoint route table

![intro](/aws-fcj/ws2/images/3.validating/endpoint_rt.png)

VPC2 endpoint interface **ssmmessages**

![intro](/aws-fcj/ws2/images/3.validating/endpoint_itf1.png)

VPC2 endpoint interface **ssm**

![intro](/aws-fcj/ws2/images/3.validating/endpoint_itf2.png)

VPC2 endpoint interface **ec2messages**

![intro](/aws-fcj/ws2/images/3.validating/endpoint_itf3.png)



**Inter-region VPC Peering**

![intro](/aws-fcj/ws2/images/3.validating/vpc_peering.png)

VPC Peering Route Table

![intro](/aws-fcj/ws2/images/3.validating/vpc_peering_rt.png)









#### II. Region US

**Internet Gateway**

![intro](/aws-fcj/ws2/images/3.validating/us_igw.png)

**All instances state**

![intro](/aws-fcj/ws2/images/3.validating/us_instance.png)

**Security Group for VPC4**

![intro](/aws-fcj/ws2/images/3.validating/us_sg_vpc4_in.png)

**Security Group for VPC5**

![intro](/aws-fcj/ws2/images/3.validating/us_sg_vpc5_in.png.png)

**Security Group for VPC6**

![intro](/aws-fcj/ws2/images/3.validating/us_sg_vpc6_in.png)

**Subnet**
![intro](/aws-fcj/ws2/images/3.validating/us_sn.png)

**Transit Gateway**

Transit Gateways

![intro](/aws-fcj/ws2/images/3.validating/us_tgw.png)

Transit Gateway Attachments

![intro](/aws-fcj/ws2/images/3.validating/us_tgw_attachment.png)

Transit Gateway Route Table Associates

![intro](/aws-fcj/ws2/images/3.validating/us_tgw_rt_ass.png)

Transit Gateway Route Table Propagations

![intro](/aws-fcj/ws2/images/3.validating/us_tgw_rt_pro.png)

Transit Gateway Route Table

![intro](/aws-fcj/ws2/images/3.validating/us_tgw_rt.png)


**Inter-region VPC Peering**

![intro](/aws-fcj/ws2/images/3.validating/us_vpc.png)

Inter-region VPC Peering Route Table

![intro](/aws-fcj/ws2/images/3.validating/us_vpc_peering_rt.png)


#### Instances
All instances state are **running**

**VPC1 instance state** 

![intro](/aws-fcj/ws2/images/3.validating/instance1.png)

**VPC2 instance state** 

![intro](/aws-fcj/ws2/images/3.validating/instance2.png)

**VPC3 instance state** 

![intro](/aws-fcj/ws2/images/3.validating/instance3.png)

**VPC4 instance state** 

![intro](/aws-fcj/ws2/images/3.validating/instance4.png)

**VPC5 instance state** 
![intro](/aws-fcj/ws2/images/3.validating/instance6.png)

**VPC6 instance state** 

![intro](/aws-fcj/ws2/images/3.validating/instance5.png)



