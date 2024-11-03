---
title : "ECS Service"
date : "`r Sys.Date()`"
weight : 3
chapter : false
pre : " <b> 3.3 </b> "
---

```terraform
resource "aws_ecs_service" "web_app_service" {
    name = "${local.project_name}_service"
    cluster = aws_ecs_cluster.web_app_cluster.id

    task_definition = aws_ecs_task_definition.web_app_task.arn
    desired_count = local.desired_count
    launch_type = "FARGATE"

    # Enable container execute command to test cpu usage
    enable_execute_command = true

    # Testing
    force_new_deployment = true

    network_configuration {
        security_groups = [aws_security_group.sg_ecs_tasks.id]
        subnets = module.vpc.private_subnets
    }

    load_balancer {
        target_group_arn = aws_alb_target_group.frontend_product.arn
        container_name = local.container_name
        container_port = local.container_port
    }

    depends_on = [aws_alb_listener.frontend_product, aws_iam_role_policy_attachment.ecs_task_execution_role_policy]

    # Code Deploy will control ECS Service
    deployment_controller {
        type = "CODE_DEPLOY"
    }
}
```