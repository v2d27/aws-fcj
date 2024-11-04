---
title : "Validating"
date :  "`r Sys.Date()`" 
weight : 5
chapter : false
pre : " <b> 5. </b> "
---

We will deploying all these configurations to AWS Cloud by Terraform:

**1.** Go to your project folder and run **`terraform init`**

```
terraform init
```

![intro](/aws-fcj/ws2/images/4.terraform/init.png)

{{%notice note%}}
Run **`terraform init`** first in any new Terraform configuration directory. It must be executed after you add or modify providers or modules.
{{%/notice%}}

**2.** Preview the changes before applying configurations by **`terraform plan`** command:

```
terraform plan
```

![intro](/aws-fcj/ws2/images/4.terraform/plan.png)

**3.** Apply the changes before applying configurations by **`terraform apply`** command. Continue to enter **`yes`** to confirm:

```
terraform apply
```

![intro](/aws-fcj/ws2/images/4.terraform/apply.png)

Please wait a few minutes to Terraform applying before validating connection.


#### Table of Contents
- [5.1 GitHub and AWS Connection](/5-validate/5.1-codestar)
- [5.2 Pipeline Result](/5-validate/5.2-pipeline)
- [5.3 Blue/Green Deployment](/5-validate/5.3-bluegreen)
- [5.4 Application Load Balancer](/5-validate/5.4-alb)