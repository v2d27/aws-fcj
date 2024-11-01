---
title : "Network Connection"
date : "`r Sys.Date()`"
weight : 1
chapter : false
pre : " <b> 8.1 </b> "
---


#### Validating Network Connection

We will access to VPC1, on-premise and VPC3 to checking VPN connection, Transit Peering connection, VPC Peering connection through each others. For VPC2 we will get access to it by Session Manager. After Terraform applying successfully, we will see the list of our necessary IP addresses here. We need public to access and validating through private IP addresses.

![intro](/aws-fcj/ws2/images/3.validating/output.png)





**1. On-premise**

Testing VPN connection from **On-premise** server to **VPC1**, **VPC2** and **VPC5**. We will use *MobaXterm* to make SSH connection to server, please choose suitably **key_perm** file for each instance.

Open your *MobaXterm* program, click on **Session** on menubar and enter your **on-premise ip address** to **remote host**, enter **ubuntu** user to **username**, check on **use private key** and select key file.

![intro](/aws-fcj/ws2/images/3.validating/on-premise-config.png)


The VPN connection status: **loaded 2, active 1** now. It means that the configuration of 2 tunnels is okey: 1 working tunnel only while the others in backup mode.

![intro](/aws-fcj/ws2/images/3.validating/ipsec.png)

Start checking connection to **VPC1**, **VPC2** and **VPC5**:

![intro](/aws-fcj/ws2/images/3.validating/on-premise-ping.png)



**2. VPC1**

We will do similarly in previous step. Enter VPC1 and check VPN, inter-region Transit peering connection to **VPC2**, **VPC5** and **on-premise**:

![intro](/aws-fcj/ws2/images/3.validating/vpc1_ping.png)

**3. VPC3 - Inter-region VPC Peering**

Following previous step, enter VPC3 to check inter-region VPC Peering connection to **VPC4**:

![intro](/aws-fcj/ws2/images/3.validating/vpc3_ping.png)

**4. Session Manager and Validating Connection**

We have configured for VPC2 as private VPC, now we will control it through HTTPS protocal and checking all connections inside:

We search **System Manager** and navigate to **Session Manager** in Node Management, click on **Start session** yellow/orange button:

![intro](/aws-fcj/ws2/images/3.validating/session_manager.png)

Choose **vpc2_instance** and click on **Start session**:

![intro](/aws-fcj/ws2/images/3.validating/session_start.png)

Testing VPN, inter-region Transit Peering connection from **VPC2** server to **VPC1**, **VPC5** and **on-premise**:

![intro](/aws-fcj/ws2/images/3.validating/vpc2_ping.png)

If your enable S3 logging for **Session Manager**, you can see all command of this session appeared in S3 Bucket. To enable S3 logging: go to **Session Manager**, choose **Preference** and enter `/logs` folder to store session log.

![intro](/aws-fcj/ws2/images/3.validating/session_log.png)

Checking Session Logs in S3 Bucket:

Go to **AWS S3 service**, choose **ssm-bucket-001** and we will see logs folder like this:

![intro](/aws-fcj/ws2/images/3.validating/s3_bucket.png)

![intro](/aws-fcj/ws2/images/3.validating/s3_log_file.png)

Check on objects and open it. We will see all session logs are stored here:

![intro](/aws-fcj/ws2/images/3.validating/s3_log_file_content.png)

{{% notice tip %}}
***Finally, we are completing this workshop here. You can log into your account and review all services if you want in next step.***
{{% /notice %}}




