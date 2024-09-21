---
title : "Customer gateways"
date : "`r Sys.Date()`"
weight : 1
chapter : false
pre : " <b> 4.1 </b> "
---

#### Customer gateways

1. Go to [VPC dashboard](https://console.aws.amazon.com/vpcconsole/)
  + Choose **Customer gateways**
  + Click at **Create customer gateway** button

![cgw](/aws-fcj/images/4.sitetositevpn/cgw-01.png)

2. At **Create customer gateway** panel:
  + In **Name tag** field: Enter **`Data-CGW`** name.
  + In **IP Address** field: Enter [Your EC2 Customer Gateway](/3-DataServer/3.6-createec2#public-customer-gateway-ip).
  + Scroll down and click on **Create customer gateway**


 
![cgw](/aws-fcj/images/4.sitetositevpn/cgw-02.png)

3. The result of creation, the state should change to **Available**.
 
![cgw](/aws-fcj/images/4.sitetositevpn/cgw-03.png)