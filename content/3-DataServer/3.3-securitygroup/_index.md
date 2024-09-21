---
title : "Create Security Group"
date : "`r Sys.Date()`"
weight : 3
chapter : false
pre : " <b> 3.3 </b> "
---

In this step, we will create the security groups used for our instances. These security groups specify to the VPC which connections are allowed or permitted. A security group acts as a virtual firewall that controls traffic for one or more instances. By default, AWS allows all outbound traffic but restricts inbound traffic. We only config the directions **inbound** in this lab.

#### I. Create security group for public subnet
Inbound rules:
   | ID     | Connection Types   | Sources               | Ports  |
   | :---:  | :---:              | :---:                 | :---:  |
   | 1.     | Ping (ICMP - IPv4) | 0.0.0.0/0 (anywhere)  |        |
   | 2.     | SSH                | 0.0.0.0/0 (anywhere)  |        |
   | 3.     | UDP (IPsec)        | 0.0.0.0/0 (anywhere)  | 500    |
   | 4.     | UDP (IPsec)        | 0.0.0.0/0 (anywhere)  | 4500   |

1. Go to **VPC Dashboard**
   + Click **Security Group**.
   + Click **Create security group**.

![SG]({{ .Site.BaseURL }}images/2.cloudserver/sg-01.png)

2. In the **Security group name** section, enter **`Data-SG-Public`**.
   + In the **Description** section, enter **`Allow IPSec, SSH, ping from internet`**.
   + In the **VPC** section, select the **Data Server** VPC.

![SG]({{ .Site.BaseURL }}images/3.dataserver/sg-01.png)

3. Config **Inbound rules**

   Allow ping connection, choose **Add rule**: 
   + In the **Type** section, choose **Custom ICMP - IPv4** to allow ping from IPv4.
   + In the **Source type** section, select **Anywhere - IPv4**.

   Allow SSH connection, choose **Add rule**: 
   + In the **Type** section, choose **SSH**.
   + In the **Source type** section, select **Anywhere - IPv4** to allow SSH from internet.

   Allow UDP (IPSec) connection, choose **Add rule**: 
   + In the **Type** section, choose **Custom UDP** to allow ping from IPv4.
   + In the **Port range** section, enter the port **`500`** to allow ping from IPv4.
   + In the **Source type** section, select **Anywhere - IPv4** to allow VPN connection from internet.

   Do the same with UDP port `500`, we create UDP port `4500`.

   And we keep **Outbound rules** as the default.

![SG]({{ .Site.BaseURL }}images/3.dataserver/sg-03.png)

   Scroll down at the bottom of page and click at **Create security group**, so we have finished creating the necessary security groups for the EC2 instances.

   You can find more information about [How does IPsec work?](https://aws.amazon.com/what-is/ipsec/) and [IPsec protocol port](https://docs.oracle.com/en/solutions/connect-oraclecloud-vmware-resources/understand-remote-access-vpn-options.html#GUID-931BA251-627B-442E-9935-FDFB4650ED72) in VPN connection.

