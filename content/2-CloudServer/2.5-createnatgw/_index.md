---
title : "Create NAT Gateway"
date : "`r Sys.Date()`"
weight : 5
chapter : false
pre : " <b> 2.5 </b> "
---

In this step, we will create NAT gateway located in Public subnet.

1. In **VPC dashboard**
    + Choose **NAT Gateways** menu.
    + Click the **Create NAT gateway** button.

![nat](/aws-fcj/images/2.cloudserver/nat-01.png)

2. In **NAT gateway settings**
    + Set **Name** field to `Cloud-NATGW`
    + In **Subnet** field, choose **Cloud-Subnet-Public**
    + Click "one time" on **Allocate Elastic IP** button to generate static IP for NAT gateway.
    + Choose IP address in dropdown list beside **Allocate Elastic IP** button.

![nat](/aws-fcj/images/2.cloudserver/nat-02.png)

  Finnally, choose **Create NAT gateway** to complete configuration. The result will be shown as below:

![nat](/aws-fcj/images/2.cloudserver/nat-03.png)
