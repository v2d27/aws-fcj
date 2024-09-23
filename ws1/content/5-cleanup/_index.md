---
title : "Clean up resources"
date : "`r Sys.Date()`"
weight : 5
chapter : false
pre : " <b> 5. </b> "
---

We will take the following steps to delete all the resources we created in this lab.
 



#### 1. Delete EC2 instances

   + Go to [EC2 instances](https://console.aws.amazon.com/ec2/home#Instances:).
   + Click **Instances**.
   + Select both **EC2-Cloud** and **EC2-Customers-Gateway** instances.
   + Click **Instance state**.
   + Click **Terminate instance**, then click **Terminate** to confirm.

![c](/aws-fcj-ws/ws1/images/5.cleanup/c-01.png)
![c](/aws-fcj-ws/ws1/images/5.cleanup/c-02.png)





#### 2. Delete NAT gateways

   + Go to [NAT gateways](https://console.aws.amazon.com/vpcconsole/home#NatGateways:).
   + Click **NAT gateways**.
   + Select **Cloud-NATGW**.
   + Click **Actions**, then click **Delete NAT gateway**.
   + Enter **`delete`** and click **Delete** to delete the NAT gateway.

![c](/aws-fcj-ws/ws1/images/5.cleanup/c-03.png)
![c](/aws-fcj-ws/ws1/images/5.cleanup/c-04.png)






#### 3. Delete Site-to-Site VPN Connections

   + Go to [Site-to-Site VPN Connections](https://console.aws.amazon.com/vpcconsole/home#VpnConnections:).
   + Select **Cloud-and-Data-VPN-Connection**.
   + Click **Actions**, then click **Delete VPN Connection**.
   + Enter **`delete`** and click **Delete** to delete the VPN Connection.

![c](/aws-fcj-ws/ws1/images/5.cleanup/c-05.png)
![c](/aws-fcj-ws/ws1/images/5.cleanup/c-06.png)






#### 4. Delete VPN gateways

   + Go to [VPG](https://console.aws.amazon.com/vpcconsole/home#VpnGateways:).
   + Select **Cloud-VPN-GW**.
   + Click **Actions**, then click **Detach from VPC**.
   + Click **Detach virtual private gateway**

![c](/aws-fcj-ws/ws1/images/5.cleanup/c-10.png)
![c](/aws-fcj-ws/ws1/images/5.cleanup/c-11.png)

   + Select **Cloud-VPN-GW** again.
   + Click **Actions**, then click **Delete virtual private gateway**.
   + Enter **`delete`** and click **Delete** to delete the VPN gateway.

![c](/aws-fcj-ws/ws1/images/5.cleanup/c-12.png)
![c](/aws-fcj-ws/ws1/images/5.cleanup/c-13.png)





#### 5. Delete Customer Gateways

   + Go to [Customer Gateways](https://console.aws.amazon.com/vpcconsole/home#CustomerGateways:).
   + Select **Data-CGW**.
   + Click **Actions**, then click **Delete customer gateway**.
   + Enter **`delete`** and click **Delete** to delete the Customer gateway.

![c](/aws-fcj-ws/ws1/images/5.cleanup/c-16.png)
![c](/aws-fcj-ws/ws1/images/5.cleanup/c-17.png)






#### 6. Delete VPCs

   + Go to [Your VPCs](https://console.aws.amazon.com/vpcconsole/home#vpcs:).
   + Select **Data Server**.
   + Click **Actions**, then click **Delete VPC**.
   + Enter **`delete`** and click **Delete** to delete the VPC.

![c](/aws-fcj-ws/ws1/images/5.cleanup/c-07.png)
![c](/aws-fcj-ws/ws1/images/5.cleanup/c-08.png)

   + Go to [Your VPCs](https://console.aws.amazon.com/vpcconsole/home#vpcs:) again.
   + Repeat previous steps to delete **Cloud Server**.

![c](/aws-fcj-ws/ws1/images/5.cleanup/c-09.png)
![c](/aws-fcj-ws/ws1/images/5.cleanup/c-14.png)






#### 7. Delete Elastic IPs

   + Go to [Elastic IPs](https://console.aws.amazon.com/vpcconsole/home#Addresses:).
   + Select **public IP address**, which is created in the [NAT gateway](/2-cloudserver/2.5-createnatgw/) step.
   + Click **Actions**, then click **Release Elastic IP address**.

![c](/aws-fcj-ws/ws1/images/5.cleanup/c-15.png)


# Everything is done!

