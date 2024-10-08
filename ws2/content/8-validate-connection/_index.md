---
title : "Validate Connection"
date :  "`r Sys.Date()`" 
weight : 8
chapter : false
pre : " <b> 8. </b> "
---

We will deploying all these configurations to AWS Cloud by Terraform:

**1.** Go to your project folder and run **`terraform init`**

![intro](/aws-fcj/ws2/images/4.terraform/init.png)

{{%notice note%}}
Run **`terraform init`** first in any new Terraform configuration directory. It must be executed after you add or modify providers or modules.
{{%/notice%}}

**2.** Preview the changes before applying configurations by **`terraform plan`** command:

![intro](/aws-fcj/ws2/images/4.terraform/plan.png)

**3.** Apply the changes before applying configurations by **`terraform apply`** command. Continue to enter **`yes`** to confirm:

![intro](/aws-fcj/ws2/images/4.terraform/apply.png)

Please wait a few minutes to Terraform applying before validating connection.

#### Contents
- [8.1 Network Connection](/8-validate-connection/8.1-network-connection)
- [8.2 Review Configurations](/8-validate-connection/8.2-review-onfiguration)