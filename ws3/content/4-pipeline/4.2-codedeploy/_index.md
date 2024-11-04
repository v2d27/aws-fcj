---
title : "AWS Code Deploy"
date : "`r Sys.Date()`"
weight : 2
chapter : false
pre : " <b> 4.2 </b> "
---

#### IAM Role for Code Deploy

```terraform
resource "aws_iam_role" "codedeploy_role" {
    name = "codedeploy_role"
    assume_role_policy = file("./templates/policies/codedeploy_role.json")
}

resource "aws_iam_policy" "codedeploy_policy" {
    name = "codedeploy_policy"
    description = "Policy for CodeDeploy to manage ECS deployments"
    policy = file("./templates/policies/codedeploy_policy.json")
}

resource "aws_iam_role_policy_attachment" "codedeploy_attachment" {
    policy_arn = aws_iam_policy.codedeploy_policy.arn
    role = aws_iam_role.codedeploy_role.name
}
```
#### Code Deploy

This Terraform configuration sets up an AWS CodeDeploy application and deployment group for deploying a web application using ECS. The application is defined to use the ECS compute platform, and the deployment group is configured for blue/green deployments with traffic control, allowing for a seamless switch between the current and new versions of the application. It includes options for handling deployment timeouts, automatic rollback in case of deployment failures, and specific settings for ECS services and load balancer configurations. The load balancer routes traffic between production and pre-production target groups, facilitating controlled deployment and testing of new versions. 

This workshop uses `CodeDeployDefault.ECSAllAtOnce` to deploy an application revision to as many instances as possible at once. You can control the routing traffic to instances process through other configurations. Understand more about it in [Working with deployment configurations in CodeDeploy](https://docs.aws.amazon.com/codedeploy/latest/userguide/deployment-configurations.html)
```terraform
resource "aws_codedeploy_app" "webapp_codedeploy" {
    name = "webapp-codedeploy"
    compute_platform = "ECS"
}

resource "aws_codedeploy_deployment_group" "webapp_deploygroup" {
    app_name = aws_codedeploy_app.webapp_codedeploy.name
    deployment_group_name = "webapp-deploygroup"
    deployment_config_name = "CodeDeployDefault.ECSAllAtOnce"
    service_role_arn = aws_iam_role.codedeploy_role.arn

    # specified BLUE_GREEN with WITH_TRAFFIC_CONTROL
    deployment_style {
        deployment_type = "BLUE_GREEN"
        deployment_option = "WITH_TRAFFIC_CONTROL"
    }

    # config blue/green deployment
    blue_green_deployment_config {
        deployment_ready_option {
            # Continue deployment when reaching timeout
            action_on_timeout = "CONTINUE_DEPLOYMENT"

            # Stop deployment when reaching timeout
            # action_on_timeout = "STOP_DEPLOYMENT"
            # wait_time_in_minutes = 2
        }

        # green_fleet_provisioning_option {
        #     action = "COPY_AUTO_SCALING_GROUP"
        # }

        terminate_blue_instances_on_deployment_success {
            action = "TERMINATE"
            # Can modify to be longer time
            termination_wait_time_in_minutes = 1
        }
    }

    # Auto Rollback Configuration
    auto_rollback_configuration {
        enabled = true
        events = ["DEPLOYMENT_FAILURE"] # "DEPLOYMENT_STOP_ON_ALARM", "DEPLOYMENT_STOP_ON_REQUEST"
    }

    # ECS Cluster
    ecs_service {
        cluster_name = aws_ecs_cluster.web_app_cluster.name
        service_name = aws_ecs_service.web_app_service.name
    }

    # Load balancer
    load_balancer_info {
        target_group_pair_info {
            prod_traffic_route {
                listener_arns = [aws_alb_listener.frontend_product.arn]
            }

            test_traffic_route {
                listener_arns = [aws_alb_listener.frontend_preproduct.arn]
            }

            target_group {
                name = aws_alb_target_group.frontend_product.name
            }

            target_group {
                name = aws_alb_target_group.frontend_preproduct.name
            }
        }
    }
}
```

Each time the CodeDeploy runs, it will read the defined parameters in "appspec.yaml" file.
