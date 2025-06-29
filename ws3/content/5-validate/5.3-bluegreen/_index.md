---
title : "Blue/Green Deployment"
date : "`r Sys.Date()`"
weight : 3
chapter : false
pre : " <b> 5.3 </b> "
---

## Blue/Green Deployment Progress

The Blue/Green deployment strategy enables seamless updates with minimal downtime by shifting traffic between two environments — "Blue" (current) and "Green" (new).

#### Deployment Preparation

The following slides show the steps involved in preparing the Green environment for deployment:

![Slide 43]( /aws-fcj/ws3/images/5.capture/Slide_43.png)  
*Creating the new task definition and preparing ECS services for deployment.*

![Slide 45]( /aws-fcj/ws3/images/5.capture/Slide_45.png)  
*Verifying the health of the Green target group and ensuring it is registered with the new tasks.*

![Slide 17]( /aws-fcj/ws3/images/5.capture/Slide_17.png)  
*Traffic shifting begins, validating the new version through load balancer testing.*

![Slide 18]( /aws-fcj/ws3/images/5.capture/Slide_18.png)  
*Monitoring the success of the traffic switch from Blue to Green and ensuring service continuity.*

---

#### Dropping Old Container

Once the Green environment is stable and fully receiving traffic, the old (Blue) version is safely terminated:

![Slide 31]( /aws-fcj/ws3/images/5.capture/Slide_31.png)  
*ECS tasks from the previous version are drained and removed to free up resources.*

---

#### Completion of Blue/Green Deployment

The deployment completes successfully after the new version proves stable and healthy:

![Slide 44]( /aws-fcj/ws3/images/5.capture/Slide_44.png)  
*Final confirmation screen showing successful cutover to Green environment.*

---

#### Container Logs

Logs from the new container version are reviewed to ensure correct startup and application behavior:

![Slide 21]( /aws-fcj/ws3/images/5.capture/Slide_21.png)  
*Application logs showing successful service initialization.*

![Slide 22]( /aws-fcj/ws3/images/5.capture/Slide_22.png)  
*Confirmation of endpoint readiness and healthy responses.*

---

By using this deployment strategy, we reduce risk, enable fast rollback, and maintain high availability during application updates.
