---
title : "Auto Scaling Group"
date : "`r Sys.Date()`"
weight : 5
chapter : false
pre : " <b> 3.5 </b> "
---

![intro](/aws-fcj/ws3/images/1.content/ecs-diagram.png)

Creating `ECS-AutoScaling.tf` file with the configurations below:

#### 1. CloudWatch Alarm

We create two CloudWatch Alarms to get metric for ECS CPU usage:
- **ecs_cpu_high**: >=70% during 60 seconds in first time.
- **ecs_cpu_low**: <=20% during 60 seconds in first time.

CloudWatch Alarm will trigger event to AutoScaling Group to scale ECS Fargate inside cluster.

```terraform
resource "aws_cloudwatch_metric_alarm" "ecs_cpu_high" {
    alarm_name = "${local.project_name}_cpu_utilization_high"
    comparison_operator = "GreaterThanOrEqualToThreshold"
    evaluation_periods = "1" # 1 times
    metric_name = "CPUUtilization"
    namespace = "AWS/ECS"
    period = "60" # seconds
    statistic = "Average"
    threshold = "70"

    dimensions = {
        ClusterName = aws_ecs_cluster.web_app_cluster.name
        ServiceName = aws_ecs_service.web_app_service.name
    }

    alarm_actions = [aws_appautoscaling_policy.up.arn]
}

resource "aws_cloudwatch_metric_alarm" "ecs_cpu_low" {
    alarm_name = "${local.project_name}_cpu_utilization_low"
    comparison_operator = "LessThanOrEqualToThreshold"
    evaluation_periods = "1" # 1 times
    metric_name = "CPUUtilization"
    namespace = "AWS/ECS"
    period = "60" # seconds
    statistic = "Average"
    threshold = "20"

    dimensions = {
        ClusterName = aws_ecs_cluster.web_app_cluster.name
        ServiceName = aws_ecs_service.web_app_service.name
    }

    alarm_actions = [aws_appautoscaling_policy.down.arn]
}
```

#### 2. AutoScaling Group

IAM Role for AutoScaling ECS service

```terraform
resource "aws_iam_role" "app_autoscale_role" {
    name = "app_autoscale_role"
    assume_role_policy = file("./templates/policies/app_autoscale_role.json")
}

resource "aws_iam_role_policy_attachment" "app_autoscale_attachment" {
  role = aws_iam_role.app_autoscale_role.name
  policy_arn = "arn:aws:iam::aws:policy/service-role/AmazonEC2ContainerServiceAutoscaleRole"
}
```

AutoScaling ECS service. This configuration sets up an auto-scaling target for an ECS service, allowing it to scale based on defined conditions. Here’s what each part does:

- Scalable Dimension: Indicates that the scaling is based on the service's desired task count (the number of running instances of the service).
- Min Capacity: Defines the minimum number of tasks (instances) the service should have running, set to 1 here. If the desired count is set higher (e.g., 2), it will start with the desired count rather than the minimum.
- Max Capacity: Sets an upper limit on the number of instances allowed, preventing the service from scaling beyond this number, which is 4 in this case.
This setup ensures that the ECS service runs with at least 1 instance but can scale up to 4 instances as needed, depending on demand and scaling policies.


```terraform
resource "aws_appautoscaling_target" "target" {
    service_namespace = "ecs"
    resource_id = "service/${aws_ecs_cluster.web_app_cluster.name}/${aws_ecs_service.web_app_service.name}"
    scalable_dimension = "ecs:service:DesiredCount"
    role_arn = aws_iam_role.app_autoscale_role.arn
    min_capacity = 1 # if min is 1 and desired is 2, it will run with 2 instances
    max_capacity = 4 # max instances running
}
```

Automatically scale capacity up by one

```terraform
resource "aws_appautoscaling_policy" "up" {
    name = "${local.project_name}_scale_up"
    service_namespace = "ecs"
    resource_id = "service/${aws_ecs_cluster.web_app_cluster.name}/${aws_ecs_service.web_app_service.name}"
    scalable_dimension = aws_appautoscaling_target.target.scalable_dimension

    step_scaling_policy_configuration {
        adjustment_type = "ChangeInCapacity"
        cooldown = 60
        metric_aggregation_type = "Maximum"

        step_adjustment {
            metric_interval_lower_bound = 0
            scaling_adjustment = 1
        }
    }

    depends_on = [aws_appautoscaling_target.target]
}
```

Automatically scale capacity down by one

```terraform
resource "aws_appautoscaling_policy" "down" {
    name = "${local.project_name}_scale_down"
    service_namespace = "ecs"
    policy_type = "StepScaling"
    resource_id = "service/${aws_ecs_cluster.web_app_cluster.name}/${aws_ecs_service.web_app_service.name}"
    scalable_dimension = aws_appautoscaling_target.target.scalable_dimension

    step_scaling_policy_configuration {
        adjustment_type = "ChangeInCapacity"
        cooldown = 60
        metric_aggregation_type = "Maximum"

        step_adjustment {
            # The difference between up and down metric
            metric_interval_upper_bound = 0
            scaling_adjustment = -1
        }
    }

    depends_on = [aws_appautoscaling_target.target]
}

```




