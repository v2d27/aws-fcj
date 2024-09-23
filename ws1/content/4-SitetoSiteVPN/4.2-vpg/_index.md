---
title : "Virtual private gateways"
date : "`r Sys.Date()`"
weight : 2
chapter : false
pre : " <b> 4.2 </b> "
---


In this step, we will create an Virtual private gateways (VPG) for **Cloud Server** VPC, which allows our instances connecting to **Data Server** in VPN. 

#### Create **VPG**

1. Go to [VPC dashboard](https://console.aws.amazon.com/vpcconsole/)
  + Choose **Virtual private gateways**
  + Click at **Create virtual private gateway** button



![vpg](/aws-fcj-ws/ws1/images/4.sitetositevpn/vpg-01.png)

2. At the **Create virtual private gateway** page.
  + In the **Name tag** field, enter the VPG name **`Cloud-VPN-GW`**
  + Click **Create virtual gateway**.

![vpg](/aws-fcj-ws/ws1/images/4.sitetositevpn/vpg-02.png)


3. Attach to **`Cloud Server`** VPC
  + In the [Virtual private gateways](https://console.aws.amazon.com/vpcconsole/home#VpnGateways:), check **Cloud-VPN-GW**
  + Click **Actions**, choose **Attach to VPC**.

![vpg](/aws-fcj-ws/ws1/images/4.sitetositevpn/vpg-03.png)

Choose **Cloud Server** at dropdown list and click **Attach to VPC**.

![vpg](/aws-fcj-ws/ws1/images/4.sitetositevpn/vpg-04.png)

We are successfull at creating VPG for **Cloud Server** VPC.

![vpg](/aws-fcj-ws/ws1/images/4.sitetositevpn/vpg-05.png)