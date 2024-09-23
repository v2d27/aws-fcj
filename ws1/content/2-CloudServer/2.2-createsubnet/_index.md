---
title : "Create Subnet"
date : "`r Sys.Date()`"
weight : 2
chapter : false
pre : " <b> 2.2 </b> "
---

#### I. Create Public Subnet for NAT Gateway
1. Create Public Subnet
    + Click **Subnets**.
    + Click **Create subnet**.

![sn](/aws-fcj-ws/ws1/images/2.cloudserver/sn-01.png)

2. At the **Create subnet** page.
    + In the **VPC ID** section, click **Cloud Server**.
    + In the **Subnet name** field, enter **`Cloud-Subnet-Public`**.
    + In the **Availability Zone** section, select the first Availability zone.
    + In the field **IPv4 CIRD block** enter **`10.10.1.0/24`**.

![sn](/aws-fcj-ws/ws1/images/2.cloudserver/sn-02.png)
![sn](/aws-fcj-ws/ws1/images/2.cloudserver/sn-03.png)

3. Scroll to the bottom of the page, click **Create subnet**. 

![sn](/aws-fcj-ws/ws1/images/2.cloudserver/sn-04.png)

4. Select **Cloud-Subnet-Public** checkbox and go to **Edit subnet settings**
    + Click **Actions**.
    + Click **Edit subnet settings**.

![sn](/aws-fcj-ws/ws1/images/2.cloudserver/sn-05.png)

5. Enable auto-assign public IPv4 address
    + Click **Enable auto-assign public IPv4 address**.
    + Click **Save**.

![sn](/aws-fcj-ws/ws1/images/2.cloudserver/sn-06.png)

#### II. Create Private Subnet for EC2 instance server

Similiar to create public subnet, we click at **Create subnet** again to create private subnet:

1. At the **Create subnet** page.
    + In the **VPC ID** section, click **Cloud Server**.
    + In the **Subnet name** field, enter **`Cloud-Subnet-Private`**.
    + In the **Availability Zone** section, select the first Availability zone.
    + In the field **IPv4 CIRD block** enter **`10.10.2.0/24`**.

![sn](/aws-fcj-ws/ws1/images/2.cloudserver/sn-10.png)

2. Scroll to the bottom of the page, click **Create subnet**. For private subnet, we do not need to **Enable auto-assign public IPv4 address**.

![sn](/aws-fcj-ws/ws1/images/2.cloudserver/sn-11.png)

Finally, we can see the state of two subnets **Available** now: **10.10.1.0/24** - public subnet and **10.10.2.0/24** - private subnet.