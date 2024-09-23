---
title : "Create Internet Gateway"
date : "`r Sys.Date()`"
weight : 4
chapter : false
pre : " <b> 2.4 </b> "
---


1. In **VPC dashboard**
    + Choose **Internet Gateways** menu.
    + Click at **Create internet gateway** button.
  
![igw](/aws-fcj/images/2.cloudserver/igw-01.png)

2. At the **Create internet gateway** page.
    + In the **Name tag** field, enter **`Cloud-IGW`**.
    + Click at **Create internet gateway** button.
  
![igw](/aws-fcj/images/2.cloudserver/igw-02.png)

3. After successful creation, tick on **Cloud-IGW** checkbox
    + Click **Actions**.
    + Choose **Attach to VPC**.
 
![igw](/aws-fcj/images/2.cloudserver/igw-03.png)

4. At the **Attach to VPC** page.
    + In the **Available VPCs** section, select **Cloud-Server**.
    + Click **Attach internet gateway** button.

![igw](/aws-fcj/images/2.cloudserver/igw-04.png)

Check the successful attaching process as shown below.

![igw](/aws-fcj/images/2.cloudserver/igw-05.png)