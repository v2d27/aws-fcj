---
title : "Site-to-Site VPN"
date :  "`r Sys.Date()`" 
weight : 1 
chapter : true
---
# AWS Site-to-Site VPN Connection

### Overall
In this lab, we will make private connection from **Database server** to **Cloud server** through the internet enviroment, using Site-to-Site VPN on AWS service. And the server inside **Cloud server** can connect to Internet via NAT Gateway.

![intro](/aws-fcj/images/1.introduce/intro-03.png)


*We will use LibreSwan to establish IPsec VPN connections for the Data Server as a Customer Gateway on AWS EC2 in this lab. You can use various methods to connect to the AWS VPN, such as simulating on VMware, EVE-NG,... or using physical routing devices that support VPNs.*



#### Table of Contents
1. [Introduce](/1-Introduce)
2. [CloudServer Configuration](/2-CloudServer)
3. [DataServer Configuration](/3-DataServer)
4. [Site-to-Site VPN](/4-SitetoSiteVPN)
5. [Clean up resources](/5-cleanup)

