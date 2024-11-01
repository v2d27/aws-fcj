---
title : "Inter-region VPC Peering"
date :  "`r Sys.Date()`" 
weight : 5
chapter : false
pre : " <b> 5. </b> "
---

## I. VPC Peering in Terraform


#### 1. VPC Peering intra-region

For the same region and the same account, **VPC peering** will auto accept connection if you have `auto_accept = true` parameter in **aws_vpc_peering_connection** resource.
Otherwise, you have to manually accept incoming connection for target vpc. You will not create **aws_vpc_peering_connection_accepter** for intra-region too.

![intro](/aws-fcj/ws2/images/2.content/vpc-peering-intra-region.png)

Terraform VPC Peering intra-region between VPC1 and VPC2 example:

```terraform
# create intra-region-vpc-peering connection
resource "aws_vpc_peering_connection" "intra-region-vpc-peering" {

    # requester VPC
    vpc_id = aws_vpc.VPC1.id

    # accepter VPC
    peer_vpc_id = aws_vpc.VPC2.id

    # automatically accept connection
    auto_accept = true 

}

```

If you want to enable private DNS resolution for vpc_peering, add `allow_remote_vpc_dns_resolution = true` attribute to both accepter and requester:
```terraform
# create intra-region-vpc-peering connection
resource "aws_vpc_peering_connection" "intra-region-vpc-peering" {

    # requester VPC
    vpc_id = aws_vpc.VPC1.id

    # accepter VPC
    peer_vpc_id = aws_vpc.VPC2.id

    # automatically accept connection
    auto_accept = true 

    accepter {
        allow_remote_vpc_dns_resolution = true
    }

    requester {
        allow_remote_vpc_dns_resolution = true
    }

}

# Remember to **Enable DNS Resolution for VPC** to work correctly.
```



#### 2. VPC Peering inter-region or cross-account

For cross-account (requester's AWS account differs from the accepter's AWS account) or inter-region VPC Peering Connections use the **aws_vpc_peering_connection** resource to manage the requester's side of the connection and use the **aws_vpc_peering_connection_accepter** resource to manage the accepter's side of the connection.

![intro](/aws-fcj/ws2/images/2.content/vpc-peering-inter-region.png)

Terraform VPC Peering inter-region between VPC1 and VPC2 example:

```terraform
# Region 1 side
resource "aws_vpc_peering_connection" "inter-region-vpc-peering" {
    provider = aws.region_singapore
    # the ID of the requester VPC
    vpc_id = aws_vpc.VPC1.id

    # Target VPC
    peer_owner_id = data.aws_caller_identity.target.account_id
    peer_vpc_id = aws_vpc.VPC2.id
    peer_region = var.region_virginia

    # for inter-region or cross-account, the auto_accept value of requester must be **false**
    auto_accept = false # default value is false, you can remove it
}

# Region 2 side
resource "aws_vpc_peering_connection_accepter" "inter-region-vpc-peering-accepter" {
    provider = aws.region_virginia

    # indicate vpc connection only
    vpc_peering_connection_id = aws_vpc_peering_connection.inter-region-vpc-peering.id
    
    # set automatically accept incoming connection here.
    auto_accept = true
}

```

To enable DNS resolution for inter-region or cross-account, we will change options in both **accepter** and **requester** of vpc peering connection. See details below:

```terraform
resource "aws_vpc_peering_connection_options" "options_requester" {
    provider = aws.region_singapore
    vpc_peering_connection_id = aws_vpc_peering_connection.inter-region-vpc-peering.id

    requester {
        allow_remote_vpc_dns_resolution = true  # enable DNS resolution for the requester VPC
    }
}

resource "aws_vpc_peering_connection_options" "options_accepter" {
    provider = aws.region_virginia
    vpc_peering_connection_id = aws_vpc_peering_connection.inter-region-vpc-peering.id

    accepter {
        allow_remote_vpc_dns_resolution = true  # enable DNS resolution for the accepter VPC
    }
}
```

You can understand more about requester and accepter through Terraform registry: [aws_vpc_peering_connection](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/vpc_peering_connection), [aws_vpc_peering_connection_accepter](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/vpc_peering_connection_accepter) and [aws_vpc_peering_connection_options](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/vpc_peering_connection_options) page.


{{%notice warning%}}
Using **accepter** and **requester** attributes in both  **aws_vpc_peering_connection** and **aws_vpc_peering_connection_options** will cause a conflict of options and overwrite the options, not update or add new options of vpc peering connection for the same VPC peering connection.
{{%/notice%}}






## II. Create inter-region VPC Peering

In this workshop, VPC3 is requester role and VPC4 is accepter role. The VPC3 will request connection to the VPC4.


![intro](/aws-fcj/ws2/images/2.content/inter-region-vpc-peering.png)





Creating `vpc-peering.tf` file with the configurations below:

```
# -------------------------------------------------------------------------------
# Create VPC Peering
# -------------------------------------------------------------------------------
# create inter-region-vpc-peering connection
resource "aws_vpc_peering_connection" "inter-region-vpc-peering" {
    provider = aws.region_singapore

    # the ID of the requester VPC
    vpc_id = aws_vpc.VPC3.id

    # Target VPC
    peer_owner_id = data.aws_caller_identity.target.account_id
    peer_vpc_id = aws_vpc.VPC4.id
    peer_region = var.region_virginia

    # accept the peering (both VPCs need to be in the same AWS account and region)
    # If two VPCs are in the same region, you only just to enable it, dont need to create accepter
    # auto_accept = true 

    tags = {
        Name = "inter-region-vpc-peering"
    }
}

# create vpc_peering_connection_accepter
resource "aws_vpc_peering_connection_accepter" "inter-region-vpc-peering-accepter" {
    provider = aws.region_virginia

    # the ID of vpc-peering connection
    vpc_peering_connection_id = aws_vpc_peering_connection.inter-region-vpc-peering.id
    
    # whether or not to accept the peering request, defaults to false.
    auto_accept = true

    tags = {
        Name = "inter-region-vpc-peering-accepter"
    }
}



# -------------------------------------------------------------------------------
# Enable DNS resolution
# -------------------------------------------------------------------------------
# enable DNS resolution for the requester VPC
resource "aws_vpc_peering_connection_options" "options_requester" {
    provider = aws.region_singapore
    vpc_peering_connection_id = aws_vpc_peering_connection.inter-region-vpc-peering.id

    requester {
        allow_remote_vpc_dns_resolution = true  # enable DNS resolution for the requester VPC
    }
}

# enable DNS resolution for the accepter VPC
resource "aws_vpc_peering_connection_options" "options_accepter" {
    provider = aws.region_virginia
    vpc_peering_connection_id = aws_vpc_peering_connection.inter-region-vpc-peering.id

    accepter {
        allow_remote_vpc_dns_resolution = true  # enable DNS resolution for the accepter VPC
    }
}


# -------------------------------------------------------------------------------
# Update necessary route table
# -------------------------------------------------------------------------------
# update route table for region_singapore
resource "aws_route" "vpc_peering_route_sin" {
    provider = aws.region_singapore
    route_table_id = aws_route_table.VPC3-RT-Public.id

    # connect to VPC4/us through vpc peering
    destination_cidr_block = var.cidr_block_vpc4
    vpc_peering_connection_id = aws_vpc_peering_connection.inter-region-vpc-peering.id
}

# update route table for region_virginia
resource "aws_route" "vpc_peering_route_us" {
    provider = aws.region_virginia
    route_table_id = aws_route_table.VPC4-RT-Private.id

    # connect to VPC3/sin through vpc peering
    destination_cidr_block = var.cidr_block_vpc3
    vpc_peering_connection_id = aws_vpc_peering_connection.inter-region-vpc-peering.id
}

```












