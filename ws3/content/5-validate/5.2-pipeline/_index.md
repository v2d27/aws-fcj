---
title : "Pipeline Result"
date : "`r Sys.Date()`"
weight : 2
chapter : false
pre : " <b> 5.2 </b> "
---

The following illustrates the complete CI/CD pipeline execution including build, deployment, and verification stages for the ECS-based application.

#### CodeBuild Stage

Build process executed via AWS CodeBuild:

![codebuild]( /aws-fcj/ws3/images/5.pipeline/codebuild.png)

---

#### CodePipeline Execution

Full pipeline execution monitored via AWS CodePipeline:

![codepipeline]( /aws-fcj/ws3/images/5.pipeline/codepipeline.png)

---

#### Build Logs

Click on the **View Details** button in the pipeline to explore build logs:

![Slide 6]( /aws-fcj/ws3/images/5.capture/Slide_6.png)

Detailed logs from CodeBuild:

![Slide 7]( /aws-fcj/ws3/images/5.capture/Slide_7.png)

---

#### Deploy Stage

After a successful build, the pipeline transitions to the deploy phase:

![Slide 8]( /aws-fcj/ws3/images/5.capture/Slide_8.png)

---

#### Deployment Status Summary

Deployment progress and health check result shown in the AWS CodeDeploy dashboard:

![Slide 9]( /aws-fcj/ws3/images/5.capture/Slide_9.png)

---

#### ECS Cluster Status

Container and task health verified in the ECS console:

![Slide 11]( /aws-fcj/ws3/images/5.capture/Slide_11.png)  
![Slide 12]( /aws-fcj/ws3/images/5.capture/Slide_12.png)  
![Slide 13]( /aws-fcj/ws3/images/5.capture/Slide_13.png)

---

#### Load Balancer Target Group Status

From the ALB target group, we observe **4 containers**:  
- 2 old tasks (Blue)  
- 2 new tasks (Green)

This is expected behavior during the Blue/Green traffic shifting phase:

![Slide 14]( /aws-fcj/ws3/images/5.capture/Slide_14.png)

---

#### Deployment Completed

Overall deployment status:

![deployment]( /aws-fcj/ws3/images/5.pipeline/deployment.png)

Details of each deployment event can be reviewed to trace progress and validation steps:

![Slide 19]( /aws-fcj/ws3/images/5.capture/Slide_19.png)

---

### Docker Image Details

The Docker image built during the pipeline was pushed to AWS Elastic Container Registry (ECR).

#### AWS ECR Overview:

![ecr]( /aws-fcj/ws3/images/5.pipeline/ecr.png)

#### Tagged Image in Repository:

![ecr_tag]( /aws-fcj/ws3/images/5.pipeline/ecr_tag.png)

This image is used in the task definition registered for deployment to ECS.

---