---
title : "Preparation"
date : "`r Sys.Date()`"
weight : 2
chapter : false
pre : " <b> 2. </b> "
---
Before you begin please ensure that: [**Terraform installed**](https://developer.hashicorp.com/terraform/tutorials/aws-get-started/install-cli).

#### 1. AWS Account

You need to collect your [AWS IAM User](https://console.aws.amazon.com/iam/home#/users) **access_key** and **secret_key** of your account. After that, creating `terraform.tfvars` file in your projects and replacing your information:

```terraform
# terraform.tfvars default loading when applying 
# if you change its name, please add arguments -var-file="[new_name].tfvars"
 
# Enter your access_key and secret_key for your account 
access_key = "[your_account_access_key]"
secret_key = "[your_account_secret_key]"
```

If you don't have already **IAM User** access key, please go to > [Create IAM User](#4-create-iam-user-optional).

{{%notice info%}}
**terraform.tfvars** file contains security credentials. Please prevent it from uploading your secret infomation by adding ***.tfvars** line in `.gitignore` if you are using git.
{{%/notice%}}


#### 2. A Project

Preparing website project. This project will be deployed on ECS environment. For me, I will use available static website named: **company-business**

You can clone [company-business](https://github.com/v2d27/aws-codepipeline) project on my github repository.

```bash
My Project Structure
├── appspec.yaml
├── build-appspec.sh
├── buildspec.yaml
├── Dockerfile
└── company-business
    └── [project-data-inside]

```

- **buildspec.yaml**: define the works that CodeBuild will do. It also call **build-appspec.sh** to update enviroment variable when completing building process. Docker will build image base on **Dockerfile** in this stage.
- **appspec.yaml**: define the works that CodeDeploy will do.



#### 3. Workshop Structure

This structure represents where files are located and all these files work together in the root module to define and manage the infrastructure as code using Terraform.

Inside **templates** folder is json template file and servies roles, policies. All these data below will be created during this workshop:

```bash
My Workshop Structure
├── .gitignore
├── ECS-AutoScaling.tf
├── ECS-main.tf
├── main.tf
├── terraform.tfvars
├── tf-environment.tf
└── templates
    ├── ecs_container.json.tpl
    └── policies
        ├── app_autoscale_role.json
        ├── codebuild_policy.json
        ├── codebuild_role.json
        ├── codedeploy_policy.json
        ├── codedeploy_role.json
        ├── codepipeline_policy.json
        ├── codepipeline_role.json
        ├── ecstask_policy.json
        └── ecstask_role.json

```


#### 4. Create IAM User [Optional]
If you do not have any IAM User, please folow below steps to create it:

Go to [AWS IAM User](https://console.aws.amazon.com/iam/home#/users), and click **Create user**:

![intro](/aws-fcj/ws3/images/2.prepare/iam_user.png)

Step 1: Enter your IAM User and click on **Next** button to continue:
![intro](/aws-fcj/ws3/images/2.prepare/iam_step1.png)

Step 2: Set permission for your IAM User.

- Choose **Attach policies directly**
- We will set **`AdministratorAccess`** permissions policy. 
- Click on **Next** button to continue:

![intro](/aws-fcj/ws3/images/2.prepare/iam_step2.png)

Step 3: Review and create. Click **Create user** to start:

![intro](/aws-fcj/ws3/images/2.prepare/iam_step3.png)

Go to inside IAM user has been created. Choose **Create access key**:

![intro](/aws-fcj/ws3/images/2.prepare/iam_4.png)

In **Create access key** page:
- Choose Use case: **Command Line Interface (CLI)**
- Choose on checkbox: **I understand the above recommendation and want to proceed to create an access key.**
- Click on **Confirmation** button to continue:

![intro](/aws-fcj/ws3/images/2.prepare/iam_5.png)

Set description tag, you can enter your description value if you want:

![intro](/aws-fcj/ws3/images/2.prepare/iam_6.png)

Finally, we can see **Access key** and **Secret access key**. Please copy two values and paste into Terraform to continue:

AWS IAM (Identity and Access Management) user’s access key and secret access key are **displayed only one times** when they are initially created. After that, you cannot retrieve the secret access key again through the AWS Management Console, AWS CLI, or any other method.

![intro](/aws-fcj/ws3/images/2.prepare/iam_7.png)

{{%notice warning%}}
If you lose your AWS access key and secret key, you will be unable to access AWS resources programmatically, and you'll need to create new keys to restore access; additionally, unauthorized users could potentially exploit the lost keys to incur charges or steal your resources. You’ll need to delete the old access key and create a new one immediately.
{{%/notice%}}



#### Contents
- [2.1 Init Environment](/2-Preparation/2.1-init-env)
- [2.2 Init IAM Roles and Policies](/2-Preparation/2.2-init-role)
- [2.3 Init ECS Task Template](/2-Preparation/2.3-init-template)