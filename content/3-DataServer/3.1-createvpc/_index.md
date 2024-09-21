---
title : "Create VPC"
date : "`r Sys.Date()`"
weight : 1
chapter : false
pre : " <b> 3.1 </b> "
---


#### Create VPC "Cloud Server"
1. Go to **VPC dashboard**
   + Click **Your VPCs**.
   + Click **Create VPC**.
   
   You can find it in the previous step [**Create VPC**](/2-CloudServer/2.1-createvpc) in **Cloud Server**

2. At the **Create VPC** page. We will create VPC only:
   + In the **Name tag** field, enter **`Data Server`**.
   + In the **IPv4 CIDR** field, enter: **`192.168.0.0/16`**.
   + Click **Create VPC**.

![vpc](/aws-fcj/images/3.dataserver/vpc-01.png)


3. If you create successfully, the state of VPC will switch to **Available**

![vpc](/aws-fcj/images/3.dataserver/vpc-02.png)

