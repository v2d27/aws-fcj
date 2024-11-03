---
title : "Auto Scaling Group"
date : "`r Sys.Date()`"
weight : 5
chapter : false
pre : " <b> 3.5 </b> "
---

Creating `ECS-AutoScaling.tf` file with the configurations below:

```terraform
################################################################################
# IAM Role for AutoScaling ECS service
################################################################################
resource "aws_iam_role" "app_autoscale_role" {
    name = "app_autoscale_role"
    assume_role_policy = file("./templates/policies/app_autoscale_role.json")
}

resource "aws_iam_role_policy_attachment" "app_autoscale_attachment" {
  role = aws_iam_role.app_autoscale_role.name
  policy_arn = "arn:aws:iam::aws:policy/service-role/AmazonEC2ContainerServiceAutoscaleRole"
}


################################################################################
# AutoScaling ECS service
################################################################################
resource "aws_appautoscaling_target" "target" {
    service_namespace = "ecs"
    resource_id = "service/${aws_ecs_cluster.web_app_cluster.name}/${aws_ecs_service.web_app_service.name}"
    scalable_dimension = "ecs:service:DesiredCount"
    role_arn = aws_iam_role.app_autoscale_role.arn
    min_capacity = 1 # if min is 1 and desired is 2, it will run with 2 instances
    max_capacity = 4 # max instances running
}

# Automatically scale capacity up by one
resource "aws_appautoscaling_policy" "up" {
    name = "${local.project_name}_scale_up"
    service_namespace = "ecs"
    resource_id = "service/${aws_ecs_cluster.web_app_cluster.name}/${aws_ecs_service.web_app_service.name}"
    scalable_dimension = "ecs:service:DesiredCount"

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

# Automatically scale capacity down by one
resource "aws_appautoscaling_policy" "down" {
    name = "${local.project_name}_scale_down"
    service_namespace = "ecs"
    resource_id = "service/${aws_ecs_cluster.web_app_cluster.name}/${aws_ecs_service.web_app_service.name}"
    scalable_dimension = "ecs:service:DesiredCount"

    step_scaling_policy_configuration {
        adjustment_type = "ChangeInCapacity"
        cooldown = 60
        metric_aggregation_type = "Maximum"

        step_adjustment {
        metric_interval_lower_bound = 0
        scaling_adjustment = -1
        }
    }

    depends_on = [aws_appautoscaling_target.target]
}

# CloudWatch alarm that triggers the autoscaling up policy
resource "aws_cloudwatch_metric_alarm" "service_cpu_high" {
    alarm_name = "${local.project_name}_cpu_utilization_high"
    comparison_operator = "GreaterThanOrEqualToThreshold"
    evaluation_periods = "1" # 1 times
    metric_name = "CPUUtilization"
    namespace = "AWS/ECS"
    period = "60" # seconds
    statistic = "Average"
    threshold = "2"

    dimensions = {
        ClusterName = aws_ecs_cluster.web_app_cluster.name
        ServiceName = aws_ecs_service.web_app_service.name
    }

    alarm_actions = [aws_appautoscaling_policy.up.arn]
    ok_actions = [aws_appautoscaling_policy.down.arn]
}
```




