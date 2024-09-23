---
title : "Create VPN connection"
date : "`r Sys.Date()`"
weight : 3
chapter : false
pre : " <b> 4.3 </b> "
---


#### **VPN Connection**

1. Go to [Site-to-Site VPN connections](https://console.aws.amazon.com/vpcconsole/home#VpnConnections:)
  + Choose **Site-to-Site VPN connections**
  + Click at **Create VPN connection** button

![vpg](/aws-fcj-ws/ws1/images/4.sitetositevpn/vpn-01.png)


2. In **Details** page.
  + Enter name of the connection: **`Cloud-and-Data-VPN-Connection`**.
  + In **Target gateway type** field: choose **Virtual private gateway**.
  + In **Virtual private gateway** field: choose **Cloud-VPN-GW**.
  + Choose **Existing** in **Customer gateway**  .
  + In **Customer gateway ID** field: choose **Data-CGW**  .
  + In **Routing options** field: choose **Static**.
  + In **Static IP prefixes** field: enter **`192.168.1.0/24`**. You can enter one or more IP prefixes in CIDR notation of **Data Server** (on-premises) separated by commas to advertise to **Cloud Server** VPC.
  + In **Local IPv4 network CIDR** field: enter **`192.168.1.0/24`**  .
  + In **Remote IPv4 network CIDR** field: enter **`10.10.2.0/24`**  .

  Scroll down and click **Create VPN connection**.



![vpg](/aws-fcj-ws/ws1/images/4.sitetositevpn/vpn-02.png)

3. Wait about 5 minutes or more to change state of VPN connection from **Pending** to **Available**.

![vpg](/aws-fcj-ws/ws1/images/4.sitetositevpn/vpn-03.png)

4. Edit **Cloud-SG-Private** security groups to allow SSH connection from CIDR: **`192.168.1.0/24`** .
  + Go to [Security Groups](https://console.aws.amazon.com/vpcconsole/home#SecurityGroups:)
  + Select **Cloud-SG-Private** and choose **Action**.
  + Click on **Edit inbound rules**.


![vpg](/aws-fcj-ws/ws1/images/4.sitetositevpn/vpn-04.png)

5. Add SSH connection.
  + Click on **Add rule**.
  + Choose **SSH** in **Type** column.
  + Choose **Custom** source and enter **`192.168.1.0/24`**.
  + Click **Save rules** to apply.

![vpg](/aws-fcj-ws/ws1/images/4.sitetositevpn/vpn-05.png)


6. Apply new **Route Propagation** for private subnet.
  + Go to [Route tables](https://console.aws.amazon.com/vpcconsole/home#RouteTables:)
  + Select **Cloud-RT-Private** and choose **Action**.
  + Click on **Edit route propagation**.

![vpg](/aws-fcj-ws/ws1/images/4.sitetositevpn/vpn-06.png)

7. Choose **Enable** in the **Propagation** column and click **Save**.

![vpg](/aws-fcj-ws/ws1/images/4.sitetositevpn/vpn-07.png)

8. My routing table after applying new **Route Propagation**.

![vpg](/aws-fcj-ws/ws1/images/4.sitetositevpn/vpn-08.png)


The next step is to configure LibreSwan to make VPN connection to AWS.