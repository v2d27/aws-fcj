---
title : "Create Subnet"
date : "`r Sys.Date()`"
weight : 2
chapter : false
pre : " <b> 3.2 </b> "
---

#### Create Public Subnet
1. Create Public Subnet
    + Click **Subnets**.
    + Click **Create subnet**.

![sn](/aws-fcj/ws1/images/2.cloudserver/sn-01.png)

2. At the **Create subnet** page.
    + In the **VPC ID** section, click **Data Server**.
    + In the **Subnet name** field, enter **`Data-Subnet-Public`**.
    + In the **Availability Zone** section, select the first Availability zone.
    + In the field **IPv4 CIRD block** enter **`192.168.1.0/24`**.

![sn](/aws-fcj/ws1/images/3.dataserver/sn-01.png)
![sn](/aws-fcj/ws1/images/3.dataserver/sn-02.png)

3. Scroll to the bottom of the page, click **Create subnet**. 

4. Select **Cloud-Subnet-Public** checkbox and go to **Edit subnet settings**
    + Click **Actions**.
    + Click **Edit subnet settings**.

![sn](/aws-fcj/ws1/images/3.dataserver/sn-03.png)

5. Enable auto-assign public IPv4 address
    + Click **Enable auto-assign public IPv4 address**.
    + Click **Save**.

![sn](/aws-fcj/ws1/images/3.dataserver/sn-04.png)