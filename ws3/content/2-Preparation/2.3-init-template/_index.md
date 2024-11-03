---
title : "Init ECS Task Template"
date : "`r Sys.Date()`"
weight : 3
chapter : false
pre : " <b> 2.3 </b> "
---

We will config ECS Task through this json template file. It contains necessary variables for ECS Task. All of them will be tranfered through Terraform variables. Our purpose is making Terraform controlling everything:



#### Init ECS Task configuration

We only just to copy and save it into `./templates/ecs_container.json.tpl` file, if you want to modify the variable name, please change inside Terraform resources **data.template_file.container_template** too:

```json
[
  {
    "name": "${container_name}",
    "image": "${app_image}",
    "essential": true,
    "cpu": ${fargate_cpu},
    "memory": ${fargate_memory},
    "networkMode": "awsvpc",
    "logConfiguration": {
        "logDriver": "awslogs",
        "options": {
          "awslogs-group": "/ecs/web-app-logs",
          "awslogs-create-group": "true",
          "awslogs-region": "${aws_region}",
          "awslogs-stream-prefix": "ecs"
        }
    },
    "portMappings": [
      {
        "containerPort": ${container_port},
        "hostPort": ${host_port},
        "protocol": "tcp"
      }
    ]
  }
]
```

More on AWS documents:
- [Amazon ECS task definition parameters](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task_definition_parameters.html)
- [Amazon ECS task definition template](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-definition-template.html)
- [Example Task Definitions](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/example_task_definitions.html) 


Finally, we completely prepare stage for Terraform. Please save it and go to next step.