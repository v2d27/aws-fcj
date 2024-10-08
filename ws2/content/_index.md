---
title : "AWS Network Connectivity with Terraform"
meta: 
date :  "`r Sys.Date()`" 
weight : 1 
chapter : true
---

# Automating AWS Network Connectivity with Terraform

###  <a name='Overview'></a>Overview
This workshop focuses on creating a automated AWS network architecture using Terraform to enable secure and efficient connectivity across multiple AWS accounts and regions. 
This design uses AWS networking solutions, including VPN Site-to-Site connections, AWS Transit Gateway, VPC Peering, providing inter-region and multi-account connection. 
Creating secure connection with AWS Systems Manager (Session Manager) and saving the history of sessions to AWS S3.

![intro](/aws-fcj/ws2/images/ws2.png?width=1000)

#### Contents
- [1. Introduction](/1-Introduce)
- [2. Preparation](/2-Preparation)
- [3. Singapore Construction](/3-sin-construction)
- [4. N.Virginia Construction](/4-us-construction)
- [5. Inter-region VPC Peering](/5-vpc-peering)
- [6. Inter-region Transit Peering](/6-transit-peering)
- [7. Transit Gateway with VPN](/7-transit-vpn)
- [8. Validate Connection](/8-validate-connection)
- [9. Clean up resources](/9-cleanup)