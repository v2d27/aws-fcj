---
title : "TGW with VPN in Terraform"
date : "`r Sys.Date()`"
weight : 1
chapter : false
pre : " <b> 6.1 </b> "
---




#### VPN Site-to-Site with Virtual Private Gateway (VPG)

When we establish a Site-to-Site VPN connection directly to a VPC, we must create a Virtual Private Gateway. We then attach this gateway to the VPC, and the VPC route tables will automatically propagate routing. We only need to **enable available propagation routing** for VPC. Please see [Create VPN Site-to-Site connection](https://v2d27.github.io/aws-fcj/ws1/4-sitetositevpn/4.3-createvpnconnection/) for more information.

#### VPN Site-to-Site with Transit Gateway (TGW)

For establishing a Site-to-Site VPN connection with Transit Gateway, we will not create attachment because VPN connection is associated with a Transit Gateway automatically. But we have to only create static route on VPC route table. It will help VPC routing the direction to TGW. **Propagation routing is not available** in this connection. 


{{%notice info%}}
All arguments including **tunnel1_preshared_key** and **tunnel2_preshared_key** will be stored in the raw state as plain-text in Terraform.
{{%/notice%}}

{{%notice note%}}
After successfully connection, please wait a short in 3 or 5 minutes to communicate with each others in both of two sides.
{{%/notice%}}