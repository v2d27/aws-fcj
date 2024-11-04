---
title : "Cluster & Task Definition"
date : "`r Sys.Date()`"
weight : 2
chapter : false
pre : " <b> 3.2 </b> "
---

#### 1. IAM Role

Grant permissions for ECS Task which is read from json file:

```terraform
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
```

Attach `AmazonECSTaskExecutionRolePolicy` to allow ecs task running command inside container.

```terraform
# IAM Policy for ECS Task can execute task
resource "aws_iam_role_policy_attachment" "ecs_task_execution_role_policy" {
    role = aws_iam_role.ecstask_role.name
    policy_arn = "arn:aws:iam::aws:policy/service-role/AmazonECSTaskExecutionRolePolicy"
}
```

#### 2. ECS and ECS Task

Define all neccessary variables first:

```terraform
locals {
    # ECR repository URL with the 'latest' tag for the web application image
    app_image = "${aws_ecr_repository.web_app_ecr.repository_url}:latest"

    # Name for the container, incorporating the project name for uniqueness
    container_name = "${local.project_name}-frontend"

    # Port on which the containerized application listens (defined in the container image)
    container_port = 80

    # Host port on which the ECS service will expose the container (mapped to container_port)
    host_port = 80

    # Port for the Application Load Balancer in the production environment
    product_port = 80

    # Port for the Application Load Balancer in the pre-production environment
    preproduct_port = 8088

    # vCPU allocation for Fargate tasks, in CPU units (256 = 0.25 vCPU)
    fargate_cpu = "256"

    # Memory allocation for Fargate tasks, in MiB
    fargate_memory = "512"

    # Desired number of running tasks in the ECS service
    desired_count = 1

    # Health check path for the load balancer to verify container health
    health_check_path = "/"
}

```

Render json template file with Terraform variables. This json file is used for container in *Task Definition*:

```terraform
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
```


Creating *ECS Cluster* and *ECS Task Definition*:

```terraform
resource "aws_ecs_cluster" "web_app_cluster" {
    name = "${local.project_name}_cluster"
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
```

Export AWS-CLI stress test command:

- Remember to change your user profile `--profile [your_IAM_user]` with your IAM user, created in this step [Create IAM User](/2-Preparation#4-create-iam-user-optional):
- **running_tasks**: list all arn of running task (no ark of task definition)
- **stress_command**: run stress test inside container of ECS cluster. This command will increase CPU usage to 100% percent during 180 seconds.



```terraform
# List all running task ARNs
output "running_tasks" {
    value = "aws ecs list-tasks --cluster ${aws_ecs_cluster.web_app_cluster.name} --region ${data.aws_region.current.id} --profile lab"
}

# Export the aws cli to test AutoScaling
output "stress_command" {
    value= "aws ecs execute-command --cluster ${aws_ecs_cluster.web_app_cluster.name} --container ${local.container_name} --command 'stress-ng --cpu 0 --timeout 180s' --interactive --region ${data.aws_region.current.id} --profile lab --task [arn_running_task]"
}
```


#### 3. Security Groups

ECS cluster runs on private subnet, so we have to setup ECS tasks that only allows inbound access from the ALB (Application Load Balancer) on the specified host port.
- The ingress block specifies that inbound access to the ECS tasks is restricted to traffic from the ALB's security group.
- Since allowing access only from the ALB's security group, no other sources can directly access the ECS tasks on that port.

```terraform
# Allow on ALB access to ECS cluster through port 80
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