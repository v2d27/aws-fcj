---
title : "Create EC2 Customer Gateway"
date : "`r Sys.Date()`"
weight : 6
chapter : false
pre : " <b> 3.6 </b> "
---

Switch to **EC2 dashboard**. Enter `EC2` in searchbox, and select it.

![ec2](/images/2.cloudserver/ec-01.png)

1. In **EC2 dashboard**
  + Click **Instances**.
  + Click **Launch instances**.

![ec2](/images/2.cloudserver/ec-02.png)


2. In the **Name and tags** field.
  + Enter **`EC2-Customer-Gateway`** to **Name**.

3. In the **Application and OS Images (Amazon Machine Image)** field.
  + Choose **Ubuntu** image with architecture **64-bit (x86)**.

![ec2](/images/3.dataserver/ec-01.png)

4. In the **Instance Type** field.
 + Click on Instance type **t2.micro**.
 + Select key pair **aws_lab**, this key is created in before step [Create EC2-Cloud](/2-CloudServer/2.7-createec2).
 
![ec2](/images/3.dataserver/ec-02.png)

5. In the **Network settings** field, click on **Edit** button.
  + In the **VPC** section, select **Data Server**.
  + In the **Subnet** section, select **Data-Subnet-Public**.
  + In the **Auto-assign Public IP** section, choose **Enable**.
  + In the **Firewall (security groups)**, select **Select an existing security group**.
  + In the **Common security section**, select security group **Data-SG-Public**.
  + Click **Launch instance** to complete.

![ec2](/images/3.dataserver/ec-03.png)

Please wait a few minutes, EC2 instance needs time to start.

![ec2](/images/3.dataserver/ec-04.png)

##### Public Customer Gateway IP
{{%notice note%}}
We need this public IP `98.81.55.104` to create **Customer Gateway** in the **Site-to-Site VPN** step.
{{%/notice%}}

##### Private Customer Gateway IP
{{%notice note%}}
We need this public IP `192.168.1.28` to create VPN connection.
{{%/notice%}}






# Connect to EC2 Customer Gateway

We must use a program that supports SSH connections with key pairs. In this lab, we recommend you choose **MobaXterm** for easily setting up SSH connections on Windows OS. It is available for download on the [MobaXterm download](https://mobaxterm.mobatek.net/download.html) page. After completely download, you have to install it. You could see these steps here [How to Install MobaXterm on Windows?](https://www.geeksforgeeks.org/how-to-install-mobaxterm-portable-edition-on-windows/).

If you prefer not to use third-party software, you can follow the steps to connect via [SSH using a PEM certificate](https://www.techgalery.com/2020/09/how-to-connect-ssh-using-pem.html) on Windows. We are also using Linux to establish SSH connections in next step this lab.

1. Open **MobaXterm** program, and click on **Session** menu.

![mb](/images/3.dataserver/mb-01.png)

2. Choose **SSH** and provide some information of our server to connect:
    + Remote host: **[your EC2-Customer-Gateway public IP address]**
    + Specify username: **`ubuntu`** 
    + Select **Advanced SSH setting** and check **Use private key**
    + Choose the path of **aws_lab.pem** key pair file. This file is created in [here](/2-CloudServer/2.7-createec2).

![mb](/images/3.dataserver/mb-02.png)

3. We are done at connecting to **EC2-Customer-Gateway**. Please keep this connection for future using.

![mb](/images/3.dataserver/mb-03.png)