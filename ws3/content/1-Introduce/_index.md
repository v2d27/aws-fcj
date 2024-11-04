---
title : "Introduction"
date :  "`r Sys.Date()`" 
weight : 1 
chapter : false
pre : " <b> 1. </b> "
---

####  1. Elastic Container Service (AWS ECS)
Amazon Elastic Container Service (ECS) is a fully managed container orchestration service that helps you to more efficiently deploy, manage, and scale containerized applications. It deeply integrates with the AWS environment to provide an easy-to-use solution for running container workloads in the cloud and on premises with advanced security features using Amazon ECS Anywhere.

![intro](/aws-fcj/ws3/images/1.content/ecs.png)

Simply describe your application and the resources required and Amazon Elastic Container Service (Amazon ECS) will launch, monitor, and scale your application across flexible compute options with automatic integrations to other supporting AWS services that your application needs. Perform system operations such as creating custom scaling and capacity rules, and observe and query data from application logs and telemetry.

#### 2. Blue/Green Deployment
*Blue/Green deployment is a deployment pattern with the intention of deploying a new version of an application without any downtime or with minimal risk. Blue/Green deployment is achieved by bringing up a similar stack and then deploying the new version of the application on this new stack. Traffic is moved from the current stack (which is called the Blue stack) to the new stack (which is called the Green stack).*

Now that we’ve covered what it is, why one should go for Blue/Green deployment?

- No downtime: You are moving the traffic from the Blue stack to the Green stack.
- Easy rollback: If the Green stack isn’t healthy, you can follow the reverse process and move the traffic back to the Blue stack.
- Reduced risk: You can validate the Green stack by running functional tests before you migrate the prod live traffic.

The below diagram shows initial deployment where only Blue tasks are running and taking 100% production traffic.

![intro](/aws-fcj/ws3/images/1.content/bg.webp)

Now, let’s look at a CodeDeploy based Blue/Green deployment.
You’ll notice from the diagram below that Green tasks start (they are the new version of the code) and are attached to Target Group 2. The ALB test traffic listener is now ready for test traffic on port 8443, test traffic will be sent to Green tasks using Target Group 2. We can add a hook (a lambda function) once test traffic is ready through the test listener. The lambda function can perform some functional testing on the ALB/test listener port 8443 and will return either “succeeded” or “failed”.

![intro](/aws-fcj/ws3/images/1.content/bg2.webp)

Assuming the test traffic lambda hook returned “succeeded,” the production traffic is routed to Target Group 2, which is in turn served by Green tasks (new code version). The ALB prod listener port 443 and test listener port 8443 both now point to Target Group 2. CodeDeploy will keep the Blue tasks for a pre-configured period so that a rollback can be possible either from the CodeDeploy console or through CLI/API call.

![intro](/aws-fcj/ws3/images/1.content/bg3.webp)

Once the pre-configured period is elapsed, CodeDeploy will terminate the Blue tasks, and after this point, rollback won’t be possible.

![intro](/aws-fcj/ws3/images/1.content/bg4.webp)


####  3. AWS services

All services in this workshop:

![intro](/aws-fcj/ws3/images/1.content/services.png)

- **Permission**: **Identity and Access Management Role (AWS IAM Role)** grants the necessary permissions and policies for all services in this workshop to function correctly.
- **Network**: **Virtual Private Cloud (AWS VPC)** creates the network environment for the ECS cluster on AWS. It initializes multiple components in the Availability Zones (AZs), including the Internet Gateway, NAT Gateway, Private/Public Subnets, Security Groups, and Routing Table. The **Application Load Balancer** distributes traffic, and **Auto Scaling** automatically scales Fargate tasks up or down. Both are created within this VPC.
- **Infrastructure**: **Elastic Container Service (AWS ECS)** is used to deploy applications running in containers on AWS Fargate.
- **Pipeline**: **AWS CodeStar** connects AWS to GitHub, enabling cloning of source code from GitHub and triggering events to AWS Pipeline. **AWS CodeBuild** builds your project, creates a Docker image, and pushes it to the AWS ECR registry. **AWS CodeDeploy** deploys the image to the AWS ECS Cluster through services and tasks. **AWS CodePipeline** orchestrates each step, stores logs, and transfers artifacts between stages.
- **Logs and Artifacts**: **AWS CloudWatch Logs** is used to store all logs from CodePipeline and ECS containers. **AWS S3** stores artifacts generated during the build process.
- **Terraform**: Terraform is an open-source tool developed by HashiCorp for Infrastructure as Code (IaC), which enables users to define and manage cloud infrastructure through code rather than manual setup or point-and-click interfaces. Terraform shortens construction time and supports complex, multi-region architectures, helping to optimize costs when using AWS services.


####  4. Estimated Cost

**1. Total Estimated Cost for 1 Hour and the pipeline runs 10 times for free-tier account:**

| Service              | Cost      |
|----------------------|-----------|
| VPC              | $0.045    |
| ECS with Fargate Task |    $0.013       |
| ECS with Fargate ALB  | $0.022    |
| Auto Scaling     | $0.00     |
| CodeStar         | $0.00     |
| CodePipeline     | $0.03 (assuming 10 executions)    |
| CodeBuild        | $0.10 (assuming 10 executions)    |
| CodeDeploy       | $0.02 (assuming 10 executions)    |
| ECR              | $0.00     |
| CloudWatch Logs  | $0.00     |
| S3               | $0.00     |
| **Total estimate cost**    | **$0.22**      |


**2. More information**

- **[AWS Identity and Access Management (IAM)](https://aws.amazon.com/iam/pricing/)**: AWS IAM is a free service that allows you to manage access to AWS services and resources securely.
- **[Amazon Virtual Private Cloud (VPC)](https://aws.amazon.com/vpc/pricing/)**: AWS VPC is a free service that enables you to launch AWS resources into a virtual network that you've defined.
- **[Elastic Container Service (ECS)](https://aws.amazon.com/ecs/pricing/)**: AWS ECS is a free service for running and managing Docker containers. You pay for the AWS resources (like EC2 instances or Fargate) that you use with ECS.
- **[AWS Fargate](https://aws.amazon.com/fargate/pricing/)**: AWS Fargate is a serverless compute engine for containers. You pay for the vCPU and memory resources that your containers use.
- **[Application Load Balancer (ALB)](https://aws.amazon.com/elasticloadbalancing/pricing/)**: AWS ALB pricing is based on the number of hours the load balancer runs and the amount of data processed.
- **[Auto Scaling](https://aws.amazon.com/autoscaling/pricing/)**: AWS Auto Scaling is a free service that automatically adjusts the number of compute resources in your application. You pay for the AWS resources that Auto Scaling provisions.
- **[AWS CodeStar/AWS CodeConnection](https://aws.amazon.com/about-aws/whats-new/2024/03/aws-codeconnections-formerly-codestar-connections/)**: AWS CodeStar and AWS CodeConnection are only the a service, which offers a unified user interface for managing software development activities. *However, on July 31, 2024, AWS discontinued support for creating and viewing CodeStar projects. For those seeking similar functionality, AWS recommends transitioning to Amazon CodeCatalyst. Currently, CodeCatalyst is only supported in the US West (Oregon) and Europe (Ireland) regions. Therefore, we will continue to use AWS CodeStar/AWS CodeConnections while awaiting the wider release of CodeCatalyst.*
- **[AWS CodePipeline](https://aws.amazon.com/codepipeline/pricing/)**: AWS CodePipeline is a free service for continuous integration and continuous delivery. You pay for the AWS resources used in your pipeline.
- **[AWS CodeBuild](https://aws.amazon.com/codebuild/pricing/)**: AWS CodeBuild is a fully managed build service. You pay for the compute resources used during the build process.
- **[AWS CodeDeploy](https://aws.amazon.com/codedeploy/pricing/)**: AWS CodeDeploy is a free service for automating code deployments.
- **[Amazon Elastic Container Registry (ECR)](https://aws.amazon.com/ecr/pricing/)**: AWS ECR pricing is based on the amount of data stored and the data transferred.
- **[Amazon CloudWatch Logs](https://aws.amazon.com/cloudwatch/pricing/)**: AWS CloudWatch Logs pricing is based on the amount of data ingested and stored.
- **[Amazon Simple Storage Service (S3)](https://aws.amazon.com/s3/pricing/)**: AWS S3 pricing is based on the amount of data stored, the number of requests, and the data transfer.




####  5. <a name='References'></a>References
+ [AWS Documentation](https://docs.aws.amazon.com/)
+ [Terraform Registry](https://registry.terraform.io/providers/hashicorp/aws/latest/docs)
+ [Guide to Connecting AWS with GitHub for Automated Workflow](https://community.aws/content/2dGy2OO7M5GOMc0gksNz46GdmLK/step-by-step-guide-to-connecting-aws-with-github-for-automated-workflow)
+ [Blue/Green Deployments on AWS](https://docs.aws.amazon.com/whitepapers/latest/blue-green-deployments/introduction.html)
+ [Blue/Green Deployments with Amazon Elastic Container Service](https://aws.amazon.com/blogs/compute/bluegreen-deployments-with-amazon-ecs/)
+ [Working with deployment configurations in CodeDeploy](https://docs.aws.amazon.com/codedeploy/latest/userguide/deployment-configurations.html)
+ [AWS VPC Terraform module](https://registry.terraform.io/modules/terraform-aws-modules/vpc/aws/latest)