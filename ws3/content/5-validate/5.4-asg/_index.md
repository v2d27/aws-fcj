---
title : "AutoScaling Group"
date : "`r Sys.Date()`"
weight : 4
chapter : false
pre : " <b> 5.4 </b> "
---

#### Validate Cloudwatch Event for AutoScaling group

- Go to **CloudWatch**, select **All alarms**
- We will see two types of alarms here:
    + One event for scaling up if CPU usage >= 70% within 1 minute.
    + Another for scaling down if CPU usage <= 20% within 1 minute.


![alarm_all]( /aws-fcj/ws3/images/5.pipeline/alarm_all.ong.png)

- Click on **webapp_cpu_utilization_high** to see detailed event, validate in **Description** column and filter in **Type** column with value equals to **Action**:

![alarm_high_trigger]( /aws-fcj/ws3/images/5.pipeline/alarm_high_trigger.png)

![alarm_high]( /aws-fcj/ws3/images/5.pipeline/alarm_high.png)

- Click on **webapp_cpu_utilization_low** to see detailed event, validate in **Description** column and filter in **Type** column with value equals to **Action**:

![alarm_low_trigger]( /aws-fcj/ws3/images/5.pipeline/alarm_low_trigger.png)

- alarm_low

![alarm_low]( /aws-fcj/ws3/images/5.pipeline/alarm_low.png)

As we can see, our application are automatically scaled up and down base on CPU usage.