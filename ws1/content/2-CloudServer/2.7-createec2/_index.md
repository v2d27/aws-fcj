---
title : "Create EC2 Server"
date : "`r Sys.Date()`"
weight : 7
chapter : false
pre : " <b> 2.7 </b> "
---

Switch to EC2 dashboard. Enter `EC2` in searchbox, and select it.

![ec2](/aws-fcj-ws/ws1/images/2.cloudserver/ec-01.png)

1. In **EC2 dashboard**
  + Click **Instances**.
  + Click **Launch instances**.

![ec2](/aws-fcj-ws/ws1/images/2.cloudserver/ec-02.png)


2. In the **Name and tags** field.
  + Enter **`EC2-Cloud`** to **Name**.
3. In the **Application and OS Images (Amazon Machine Image)** field.
  + Choose **Ubuntu** image with architecture **64-bit (x86)**.
![ec2](/aws-fcj-ws/ws1/images/2.cloudserver/ec-03.png)

4. In the **Instance Type** field.
 + Click on Instance type **t2.micro**.
 + And click on **Create new key pair** button.
 
![ec2](/aws-fcj-ws/ws1/images/2.cloudserver/ec-04.png)

5. In the **Create key pair** field, enter the key name to connect to server.
 + Enter **`aws_lab`** to **Key pair name**
 + And click on **Create new key pair** button.
 + Remember to save the key in your local computer for future using.

![ec2](/aws-fcj-ws/ws1/images/2.cloudserver/ec-05.png)

5. In the **Network settings** field, click on **Edit** button.
  + In the **VPC** section, select **Cloud Server**.
  + In the **Subnet** section, select **Cloud-Subnet-Private**.
  + In the **Auto-assign Public IP** section, uncheck it.
  + In the **Firewall (security groups)**, select **Select an existing security group**.
  + In the **Common security section**, select security group **Cloud-SG-Private**.
  + Click **Launch instance** to complete.

![ec2](/aws-fcj-ws/ws1/images/2.cloudserver/ec-06.png)

Please wait a few minutes, EC2 instance needs time to start.

![ec2](/aws-fcj-ws/ws1/images/2.cloudserver/ec-07.png)


##### Private IP EC2-Cloud address

{{%notice note%}}
We need this private IP `10.10.2.162` for testing connection later.
{{%/notice%}}