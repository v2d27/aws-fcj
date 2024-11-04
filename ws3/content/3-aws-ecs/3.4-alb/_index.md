---
title : "Application Load Balancer"
date : "`r Sys.Date()`"
weight : 4
chapter : false
pre : " <b> 3.4 </b> "
---

#### 1. Application Load Balancer (ALB)
Create internet application load balancer

```terraform
resource "aws_alb" "web_app_alb" {
    name = "${local.project_name}-alb"
    subnets = module.vpc.public_subnets
    security_groups = [aws_security_group.sg_alb.id]
    load_balancer_type = "application"
    internal = false
    idle_timeout = 60
}
```
#### 2. Application Load Balancer Listener

Application Load Balancer will listen in two ports:

- Port 80: for running product environment (blue port)
- Port 8088: for testing preproduct environment (green port)

The listener will forward all traffic to Target group without any conditions.

```terraform
# Listener both 80 port
resource "aws_alb_listener" "frontend_product" {
    load_balancer_arn = aws_alb.web_app_alb.arn
    port = local.product_port
    protocol = "HTTP"

    # in default_action, ALB will point to target_group "product"
    default_action {
        target_group_arn = aws_alb_target_group.frontend_product.arn
        type = "forward"
    }
}

# Listener both 8088 port
resource "aws_alb_listener" "frontend_preproduct" {
    load_balancer_arn = aws_alb.web_app_alb.arn
    port = local.preproduct_port
    protocol = "HTTP"

    # in default_action, ALB will point to target_group "product"
    default_action {
        target_group_arn = aws_alb_target_group.frontend_preproduct.arn
        type = "forward"
    }
}
```
#### 3. Target Groups

Create Target groups for ALB and define health check time. We will create the same configurations for two target groups to deploy with blue/green deployment strategy. 
More on Terraform registry [aws_alb_target_group](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/lb_target_group).

```terraform
# Target group for ALB
resource "aws_alb_target_group" "frontend_product" {
    name = "${local.project_name}-frontend-product"
    port = local.host_port
    protocol = "HTTP"
    vpc_id = module.vpc.vpc_id
    target_type = "ip"

    health_check {
        healthy_threshold = "3"
        interval = "5" # health check each 5s
        protocol = "HTTP"
        matcher = "200,404"
        timeout = "2"
        path = local.health_check_path
        unhealthy_threshold = "2"
    }
}

resource "aws_alb_target_group" "frontend_preproduct" {
    name = "${local.project_name}-frontend-preproduct"
    port = local.host_port
    protocol = "HTTP"
    vpc_id = module.vpc.vpc_id
    target_type = "ip"

    health_check {
        healthy_threshold = "3"
        interval = "5" # health check each 5s
        protocol = "HTTP"
        matcher = "200,404"
        timeout = "2"
        path = local.health_check_path
        unhealthy_threshold = "2"
    }
}
```


#### 4. Security Groups

Security Groups for ALB to allow listen on port 80 (product) and port 8088 (preproduct) from anywhere:

```terraform
resource "aws_security_group" "sg_alb" {
    name = "sg_alb"
    description = "Allow inbound access from the internet"
    vpc_id = module.vpc.vpc_id

    ingress {
        protocol = "tcp"
        from_port = local.product_port
        to_port = local.product_port
        cidr_blocks = ["0.0.0.0/0"]
        description = "ALB listener product port"
    }

    ingress {
        protocol = "tcp"
        from_port = local.preproduct_port
        to_port = local.preproduct_port
        cidr_blocks = ["0.0.0.0/0"]
        description = "ALB listener preproduct port"
    }

    egress {
        protocol = "-1"
        from_port = 0
        to_port = 0
        cidr_blocks = ["0.0.0.0/0"]
    }
}
```