---
title : "Create Internet Gateway"
date : "`r Sys.Date()`"
weight : 4
chapter : false
pre : " <b> 3.4 </b> "
---


1. In **VPC dashboard**
    + Choose **Internet Gateways** menu.
    + Click at **Create internet gateway** button.
  
![igw](/images/2.cloudserver/igw-01.png)

2. At the **Create internet gateway** page.
    + In the **Name tag** field, enter **`Data-IGW`**.
    + Click at **Create internet gateway** button.
  
![igw](/images/3.dataserver/igw-01.png)

3. After successful creation, tick on **Data-IGW** checkbox
    + Click **Actions**.
    + Choose **Attach to VPC**.
 
![igw](/images/3.dataserver/igw-03.png)

4. At the **Attach to VPC** page.
    + In the **Available VPCs** section, select **Data Server**.
    + Click **Attach internet gateway** button.

![igw](/images/3.dataserver/igw-02.png)