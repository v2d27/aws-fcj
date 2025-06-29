---
title : "GitHub and AWS Connection"
date : "`r Sys.Date()`"
weight : 1
chapter : false
pre : " <b> 5.1 </b> "
---

#### 1. Setup AWS Connector for GitHub

First, go to [GitHub Marketplace](https://github.com/marketplace):
- Find verified "AWS Connector for GitHub" application
- Click on it

![github-market](/aws-fcj/ws3/images/5.validating/github-market.png)

Next, srolling down at bottom page, click **Install it for free** button:

![intro](/aws-fcj/ws3/images/5.validating/aws-connector-app.png)
![aws-connector-install](/aws-fcj/ws3/images/5.validating/aws-connector-install.png)

Input some Billing information and click **Save** button:

![aws-connector-order](/aws-fcj/ws3/images/5.validating/aws-connector-order.png)

At review your orther page, click **Install other and begin installation** button to install:

![aws-connector-order-complete](/aws-fcj/ws3/images/5.validating/aws-connector-order-complete.png)

Next, grant perrmission for "AWS Connector for GitHub" application. You can specific particularly repository or allow to access all repositories. Click **Install & Authorize** buton:

![aws-connector-authorize](/aws-fcj/ws3/images/5.validating/aws-connector-authorize.png)

Verify installation at [GitHub Application](https://github.com/settings/apps/authorizations.png):

![aws-connector-github-authorize](/aws-fcj/ws3/images/5.validating/aws-connector-github-authorize.png)

#### 2. Authorize on AWS Connection/AWS CodeStar

Go to [AWS Connection](https://ap-southeast-1.console.aws.amazon.com/codesuite/settings/connections?region=ap-southeast-1&connections-meta=eyJmIjp7InRleHQiOiIifSwicyI6e30sIm4iOjIwLCJpIjowfQ) inside **AWS CodePipeline** setting:

- Choose **connection name** and click on **Update pending connection**:
- After connecting successfully, status change from *Pending* to *Available*.

![intro](/aws-fcj/ws3/images/5.validating/connection.png)


