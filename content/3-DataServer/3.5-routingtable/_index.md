---
title : "Create Routing Table"
date : "`r Sys.Date()`"
weight : 5
chapter : false
pre : " <b> 3.5 </b> "
---


We will create a table **Data-RT-Public**, routing **[Data-Subnet-Public](/3-DataServer/3.2-createsubnet)** subnet to **[Data-IGW](/3-DataServer/3.4-createigw)** internet gateway.

#### Create route table public

In **VPC dashboard**
  + Choose **Route tables** menu.
  + Click the **Create route table** button.

![rts](/images/2.cloudserver/rt-01.png)

2. At the **Create route table** page.
    + In the **Name** field, enter **`Data-RT-Public`**.
    + In the **VPC** section, select **Data Server**.
    + Click **Create route table**.

![rts](/images/3.dataserver/rts-01.png)

3. After creating the route table successfully.
  + Click **Edit routes**.

![rts](/images/3.dataserver/rts-02.png)


4. At the **Edit routes** page.
  + Click **Add route**.
  + In the **Destination** field, enter `0.0.0.0/0`
  + In the **Target** section, select **Internet Gateway** and then select **Data-IGW**.
  + Click **Save changes**.

![rts](/images/3.dataserver/rts-03.png)

5. Click the **Subnet associations** tab.
  + Click **Edit subnet associations** to proceed with the associate custom route table we just created in **Data-Subnet-Public**.

![rts](/images/3.dataserver/rts-04.png)

6. At the **Edit subnet associations** page.
  + Click on **Data-Subnet-Public**.
  + Click **Save associations**.

![rts](/images/3.dataserver/rts-05.png)
