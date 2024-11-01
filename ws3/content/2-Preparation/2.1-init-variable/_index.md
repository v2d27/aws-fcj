---
title : "Initialization Variables"
date : "`r Sys.Date()`"
weight : 1
chapter : false
pre : " <b> 2.1 </b> "
---

We will set up necessary variables for Terraform can understand it. With variable block, this is global variable that you can use it in anywhere in Terraform.

Terraform will load all files ***.tf** format in root module, so you can name the file whichever you want. Now, we will create **tf-variables.tf** file with all content in this page:

#### Init Account
We have some security credentials in previous step. We need to load it into Terraform:

```terraform
# account 1
variable "access_key_1" {}
variable "secret_key_1" {}

# account 2
variable "access_key_2" {}
variable "secret_key_2" {}
```

#### Init Region
I choose two regions Singapore and Virginia. You can change it if you want:
```terraform
# region 1
variable "region_singapore" {
  type = string
  default = "ap-southeast-1"
}

# region 2
variable "region_virginia" {
  type = string
  default = "us-east-1"
}
```

#### PSK VPN Site-to-Site
A PSK VPN (Pre-Shared Key Virtual Private Network) is a type of VPN that uses a pre-shared key (PSK) for authentication. This key is shared in advance between the VPN server and the client before establishing a secure connection.

**Character Requirements** : The PSK must consist of ASCII characters only. You can use a mix of uppercase letters, lowercase letters, numbers, and special characters.
AWS recommends avoiding simple patterns or easily guessable keys (e.g., avoid common words or sequences like "12345678").
The maximum length of the PSK is 128 characters. AWS requires the PSK to be at least 8 characters long.

We will custom PSK to automate setup vpn connection.

```terraform
# custom psk for vpn connection
variable "psk" {
  description = "Optional preshared_key for vpn tunnel 1 and vpn tunnel 2"
  type = list(string)
  default = [ "TT1KRlvnxbk8Hy8SG3m8Cj.zebPvCQ40cPTtqCC2mmPfh6y37XkFXRBft0RF", "2fDfA535eW4Av7dApfpMhyh6WR7CfOvaiGOSDTuCcb5DjuCr6_chWHIzVFHA" ]
}
```

#### Network and Subnet

AWS supports IPv4 CIDR range blocks from /16 to /28.
When creating a VPC, you can specify any IPv4 CIDR block in the private IP ranges as defined by RFC 1918:

**- 10.0.0.0/8 (10.0.0.0 to 10.255.255.255)**

**- 172.16.0.0/12 (172.16.0.0 to 172.31.255.255)**

**- 192.168.0.0/16 (192.168.0.0 to 192.168.255.255)**

This is my settings. Remember to change subnet cidr too if you change vpc cidr.


```terraform
variable "cidr_block_onpremise" {
  type = string
  default = "192.168.0.0/16"
}

variable "cidr_block_allvpc" {
  type = string
  default = "10.0.0.0/8"
}

variable "cidr_block_anywhere" {
  type = string
  default = "0.0.0.0/0"
}

variable "cidr_block_vpc1" {
  type = string
  default = "10.11.0.0/16"
}

variable "subnet_public_vpc1" {
  type = string
  default = "10.11.1.0/24"
}

variable "cidr_block_vpc2" {
  type = string
  default = "10.12.0.0/16"
}

variable "subnet_private_vpc2" {
  type = string
  default = "10.12.1.0/24"
}

variable "cidr_block_vpc3" {
  type = string
  default = "10.13.0.0/16"
}

variable "subnet_public_vpc3" {
  type = string
  default = "10.13.1.0/24"
}

variable "cidr_block_vpc4" {
  type = string
  default = "10.22.0.0/16"
}

variable "subnet_private_vpc4" {
  type = string
  default = "10.22.1.0/24"
}

variable "cidr_block_vpc5" {
  type = string
  default = "10.25.0.0/16"
}

variable "subnet_private_vpc5" {
  type = string
  default = "10.25.1.0/24"
}

variable "subnet_public_vpc6" {
  type = string
  default = "192.168.1.0/24"
}
```

Finally, we completely set up necessary variables for Terraform. Please save it and go to next step.