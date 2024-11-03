---
title : "ECS Task"
date : "`r Sys.Date()`"
weight : 2
chapter : false
pre : " <b> 3.2 </b> "
---

#### 1. IAM Role

Grant permissions for ECS Task which is read from json file and add more an AmazonECSTaskExecutionRolePolicy:

```terraform
################################################################################
# IAM Role for ECS Task
################################################################################
resource "aws_iam_role" "ecstask_role" {
    name = "ecstask_role"
    assume_role_policy = file("./templates/policies/ecstask_role.json")
}

resource "aws_iam_policy" "ecstask_policy" {
    name = "ecstask_policy"
    description = "Policy granting read/write access to ECR repositories"
    policy = file("./templates/policies/ecstask_policy.json")
}

resource "aws_iam_role_policy_attachment" "ecr_policy_attachment" {
    role = aws_iam_role.ecstask_role.name
    policy_arn = aws_iam_policy.ecstask_policy.arn
}

# IAM Policy for ECS Task can execute task
resource "aws_iam_role_policy_attachment" "ecs_task_execution_role_policy" {
    role = aws_iam_role.ecstask_role.name
    policy_arn = "arn:aws:iam::aws:policy/service-role/AmazonECSTaskExecutionRolePolicy"
}
```

#### ECS and ECS Task

```terraform
locals {
    app_image = "${aws_ecr_repository.web_app_ecr.repository_url}:latest"
    container_name = "${local.project_name}-frontend"
    container_port = 80 # image
    host_port = 80 # ECS
    product_port = 80 # Application Load Balancer for product environment
    preproduct_port = 8088 # Application Load Balancer for pre-product environment
    fargate_cpu = "256"
    fargate_memory = "512"
    desired_count = 1
    health_check_path = "/"
}

################################################################################
# ECS
################################################################################
resource "aws_ecs_cluster" "web_app_cluster" {
    name = "${local.project_name}_cluster"
}

# Render json file with custom variable
data "template_file" "container_template" {
    template = file("./templates/ecs_container.json.tpl")
    vars = {
        container_name = local.container_name
        app_image = local.app_image
        container_port = local.container_port
        host_port = local.host_port
        fargate_cpu = local.fargate_cpu
        fargate_memory = local.fargate_memory
        aws_region = local.region
    }
}

resource "aws_ecs_task_definition" "web_app_task" {
    family = "${local.project_name}-task"

    # ECS Task permission when deploying
    task_role_arn = aws_iam_role.ecstask_role.arn

    # Fargate permission when running
    execution_role_arn = aws_iam_role.ecstask_role.arn


    network_mode = "awsvpc"
    requires_compatibilities = ["FARGATE"]
    cpu = local.fargate_cpu
    memory = local.fargate_memory
    container_definitions = data.template_file.container_template.rendered
}

output "ecs_container_execute_cmd" {
    description = "Execute the command to containter in ECS"
    value= "aws ecs execute-command --cluster ${aws_ecs_cluster.web_app_cluster.name} --task ${aws_ecs_task_definition.web_app_task.id} --container ${local.project_name} --command \"/bin/sh\" --interactive"
}
```


#### Security Groups

```terraform
# Traffic to the ECS cluster should only come from the ALB
resource "aws_security_group" "sg_ecs_tasks" {
    name = "sg_ecs_tasks"
    description = "Allow inbound access from the ALB only"
    vpc_id = module.vpc.vpc_id

    ingress {
        protocol = "tcp"
        from_port = local.host_port
        to_port = local.host_port
        security_groups = [aws_security_group.sg_alb.id]
        description = "Allow access ECS Host port from only ALB"
    }

    egress {
        protocol = "-1"
        from_port = 0
        to_port = 0
        cidr_blocks = ["0.0.0.0/0"]
    }
}
```