---
title : "Introduction"
date :  "`r Sys.Date()`" 
weight : 1 
chapter : false
pre : " <b> 1. </b> "
---
A **VPN (Virtual Private Network)** creates a private network connection between devices through the internet. VPNs are used to safely and anonymously transmit data over public networks. They work by masking user IP addresses and encrypting data so it's unreadable by anyone not authorized to receive it.

#### What is a VPN used for?
VPN services are mainly used to safely send data over the internet. The three main functions of VPNs are:

**1. Privacy**  
Without a virtual private network, your personal data like passwords, credit card information, and browsing history can be recorded and sold by third parties. VPNs use encryption to keep this confidential information private, especially when connecting over public wi-fi networks.  

**2. Anonymity**  
Your IP address contains information about your location and browsing activity. All websites on the Internet track this data using cookies and similar technology. They can identify you whenever you visit them. A VPN connection hides your IP address so that you remain anonymous on the Internet.  

**3. Security**  
A VPN service uses cryptography to protect your internet connection from unauthorized access. It can also act as a shut-down mechanism, terminating pre-selected programs in case of suspicious internet activity. This decreases the likelihood of data being compromised. These features allow companies to give remote access to authorized users over their business networks.

#### How many types of VPN?
![intro](/aws-fcj/images/1.introduce/intro-01.png)
The four types of VPN are:

**1. Personal VPN**: enable individuals to establish secure and private connections to the open Internet.

**2. Remote access VPN**: provide remote access for the individual computers to a private network.

**3. Mobile VPN**: allow you to connect to a local network from mobile devices, ensure the encrypted protection of data, and are useful in conditions of the absence consistent or stable internet connection.

**4. Site-to-site VPN**: connect to networks and enable organizations to combine several networks from different locations into a single network (intranet). 

These are own networks, for example, two offices of the same company, geographically remoted, or also networks of partner companies (extranet). The main goal is to provide access to resources for multiple users in various fixed locations. 

They are incredibly useful in large-scale business environments to ensure secure communication and sharing of information and resources between departments all over the world. These VPNs provide confidentiality by creating an encrypted tunnel and encrypting data to protect them from unauthorized access.

#### Site-to-site VPN on AWS

In this lab, we will explore Site-to-Site VPN, a service provided by AWS. To estabish Site-to-Site VPN connection, it works base on two dependencies: **Customer gateways** and **Virtual private gateways**.
![intro](/aws-fcj/images/1.introduce/intro-02.png)
+ **Customer gateways (CGW)**: The CGW serves as the customer’s endpoint for the VPN connection, representing the on-premises side that connects to AWS. 
Typically, the CGW is a physical device (such as a router or firewall) or a software application situated within the on-premises network infrastructure.
+ **Virtual private gateway (VGW)**: The VGW is part of a VPC that provides edge routing for AWS managed VPN connections and AWS Direct Connect connections. You associate an AWS Direct Connect gateway with the virtual private gateway for the VPC.

#### Site-to-Site VPN Connection Pricing on AWS

AWS caculates Site-to-Site VPN connection following by: `the number` and `the duration` time of connection. This is applied for all customers, include *free-tier*:

***$0.05 per Site-to-Site VPN connection per hour***

Data transfer-in through the connection is free, but data transfer-out is only free up to 100GB each month for you. Our purpose is only hands-on lab work, so you don't need to worry much about additional costs.

For more infomation and to understand how AWS caculates, please visit [AWS Site-to-Site Pricing](https://aws.amazon.com/vpn/pricing/) page.

#### Hands-on lab

We will establish AWS services follow by each region of the overall diagram below:
![intro](/aws-fcj/images/1.introduce/intro-03.png)


#### Table of Contents
1. [Introduce](/1-Introduce)
2. [CloudServer Configuration](/2-CloudServer)
3. [DataServer Configuration](/3-DataServer)
4. [Site-to-Site VPN](/4-SitetoSiteVPN)
5. [Clean up resources](/5-cleanup)