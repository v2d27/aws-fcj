---
title : "Create Routing Table"
date : "`r Sys.Date()`"
weight : 6
chapter : false
pre : " <b> 2.6 </b> "
---


We will create two tables **Cloud-RT-Public** and **Cloud-RT-Private**:
  - **Cloud-RT-Public**: Routing **Cloud-Subnet-Public** to **Cloud-IGW** internet gateway.
  - **Cloud-RT-Private**: Routing **Cloud-Subnet-Private** to **Cloud-NATGW** NAT gateway.

#### I. Create route table public

In **VPC dashboard**
  + Choose **Route tables** menu.
  + Click the **Create route table** button.

![rt](/aws-fcj/ws1/images/2.cloudserver/rt-01.png)

2. At the **Create route table** page.
    + In the **Name** field, enter **`Cloud-RT-Public`**.
    + In the **VPC** section, select **Cloud Server**.
    + Click **Create route table**.

![rt](/aws-fcj/ws1/images/2.cloudserver/rt-02.png)

3. After creating the route table successfully.
  + Click **Edit routes**.

![rt](/aws-fcj/ws1/images/2.cloudserver/rt-03.png)


4. At the **Edit routes** page.
  + Click **Add route**.
  + In the **Destination** field, enter `0.0.0.0/0`
  + In the **Target** section, select **Internet Gateway** and then select **Cloud-IGW**.
  + Click **Save changes**.

![rt](/aws-fcj/ws1/images/2.cloudserver/rt-04.png)

![rt](/aws-fcj/ws1/images/2.cloudserver/rt-05.png)

5. Click the **Subnet associations** tab.
  + Click **Edit subnet associations** to proceed with the associate custom route table we just created in **Cloud-Subnet-Public**.

![rt](/aws-fcj/ws1/images/2.cloudserver/rt-07.png)

6. At the **Edit subnet associations** page.
  + Click on **Cloud-Subnet-Public**.
  + Click **Save associations**.

![rt](/aws-fcj/ws1/images/2.cloudserver/rt-06.png)


7. Check that the route table information has been associated with **Cloud-Subnet-Public** and the internet route information has been pointed to the Internet Gateway as shown below.

![rt](/aws-fcj/ws1/images/2.cloudserver/rt-08.png)



#### II. Create route table private

In **VPC dashboard**
  + Choose **Route tables** menu.
  + Click the **Create route table** button.

![rt](/aws-fcj/ws1/images/2.cloudserver/rt-01.png)

2. At the **Create route table** page.
    + In the **Name** field, enter **`Cloud-RT-Private`**.
    + In the **VPC** section, select **Cloud Server**.
    + Click **Create route table**.

![rt](/aws-fcj/ws1/images/2.cloudserver/rt-10.png)

3. After creating the route table successfully.
  + Click **Edit routes**.

![rt](/aws-fcj/ws1/images/2.cloudserver/rt-11.png)


4. At the **Edit routes** page.
  + Click **Add route**.
  + In the **Destination** field, enter `0.0.0.0/0`
  + In the **Target** section, select **NAT Gateway** and then select **Cloud-NATGW**.
  + Click **Save changes**.

![rt](/aws-fcj/ws1/images/2.cloudserver/rt-12.png)

5. Click the **Subnet associations** tab.
  + Click **Edit subnet associations** to proceed with the associate custom route table we just created in **Cloud-Subnet-Private**.

![rt](/aws-fcj/ws1/images/2.cloudserver/rt-13.png)

6. At the **Edit subnet associations** page.
  + Click on **Cloud-Subnet-Private**.
  + Click **Save associations**.

![rt](/aws-fcj/ws1/images/2.cloudserver/rt-14.png)


7. Check that the route table information has been associated with **Cloud-Subnet-Private** and the internet route information has been pointed to the Internet Gateway as shown below.

![rt](/aws-fcj/ws1/images/2.cloudserver/rt-15.png)