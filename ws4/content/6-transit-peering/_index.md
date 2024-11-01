---
title : "Inter-region Transit Peering"
date :  "`r Sys.Date()`" 
weight : 6
chapter : false
pre : " <b> 6. </b> "
---

## I. Inter-region Transit Peering in Terraform
We have two Transit Gateways. We need to determine which one is the requester and which one is the accepter. For three or more Transit Gateways, you should designate one Transit Gateway as the primary node to simplify infrastructure management. All remaining Transit Gateways will be accepters. The setup depends on your specific configuration, so choose suitable solutions for each particular situation.


Here is an example to create TGW peering in cross-acocunt. In case you want to connect TGW in the same account, you can remove `peer_account_id` attribute:

For **TGW peering requester**:

```terraform
# Create TGW peering requester
resource "aws_ec2_transit_gateway_peering_attachment" "tgw_peering" {
    provider = aws.region_singapore

    # TGW requester id
    transit_gateway_id = aws_ec2_transit_gateway.my-tgw-1.id

    # Target TGW
    peer_account_id = data.aws_caller_identity.target.account_id
    peer_region = var.region_virginia  
    peer_transit_gateway_id = aws_ec2_transit_gateway.my-tgw-2.id
}
```

For **TGW peering accepter**:

```terraform
# Create TGW peering accepter
resource "aws_ec2_transit_gateway_peering_attachment_accepter" "tgw_peering_accepter" {
    provider = aws.region_virginia

    # Poiting to TGW requester
    transit_gateway_attachment_id = aws_ec2_transit_gateway_peering_attachment.tgw_peering.id
}
```



{{%notice note%}}
The Transit Gateway itself does not directly support DNS resolution across VPCs or regions. However, you can still achieve DNS resolution between VPCs connected to a Transit Gateway by configuring your VPC settings and using Route 53 for cross-VPC DNS resolution.
{{%/notice%}}


## II. Creating Inter-region Transit Peering


![intro](/aws-fcj/ws2/images/2.content/tgw-peering.png)


Creating `transit-peering.tf` file with the configurations and updating table for **TGW route table** and **VPC route table** as shown below:

#### TGW Requester

```terraform
#--------------------------------------------------------------------------------
# Region Singapore: Requester
#--------------------------------------------------------------------------------
# Create Transit Gateway Peering Attachment
resource "aws_ec2_transit_gateway_peering_attachment" "tgw_peering" {
    provider = aws.region_singapore
    transit_gateway_id = aws_ec2_transit_gateway.my-tgw-1.id

    # Target transit gateway
    peer_account_id = data.aws_caller_identity.target.account_id
    peer_region = var.region_virginia  
    peer_transit_gateway_id = aws_ec2_transit_gateway.my-tgw-2.id

    tags = {
        Name = "tgw_peering"
    }
}

# update TGW route table to TGW peering
resource "aws_ec2_transit_gateway_route" "tgw1_rt_route_peering" {
    provider = aws.region_singapore

    # Routing to VPC5
    destination_cidr_block = var.cidr_block_vpc5 
    transit_gateway_route_table_id = aws_ec2_transit_gateway.my-tgw-1.association_default_route_table_id
    transit_gateway_attachment_id = aws_ec2_transit_gateway_peering_attachment.tgw_peering.id
}
```

For requester, the default **transit_gateway_route_table** only point to VPC5 where **cidr_block** of inside target Transit Gateway.

#### TGW Accepter

```terraform
#--------------------------------------------------------------------------------
# Region Virginia: Accepter
#--------------------------------------------------------------------------------
resource "aws_ec2_transit_gateway_peering_attachment_accepter" "tgw_peering_accepter" {
    provider = aws.region_virginia

    # Poiting to TGW requester
    transit_gateway_attachment_id = aws_ec2_transit_gateway_peering_attachment.tgw_peering.id

    tags = {
        Name = "tgw_peering_accepter"
    }
}

# update TGW route table to TGW peering
resource "aws_ec2_transit_gateway_route" "tgw2_rt_route_peering" {
    provider = aws.region_virginia

    # Routing to all VPCs which are connected to Transit Gateway
    destination_cidr_block = var.cidr_block_allvpc  
    transit_gateway_route_table_id = aws_ec2_transit_gateway.my-tgw-2.association_default_route_table_id
    transit_gateway_attachment_id = aws_ec2_transit_gateway_peering_attachment_accepter.tgw_peering_accepter.id
}

# update TGW route table to TGW peering
resource "aws_ec2_transit_gateway_route" "tgw2_rt_route_onpremise" {
    provider = aws.region_virginia

    # Routing to on-premise
    destination_cidr_block = var.cidr_block_onpremise
    transit_gateway_route_table_id = aws_ec2_transit_gateway.my-tgw-2.association_default_route_table_id
    transit_gateway_attachment_id = aws_ec2_transit_gateway_peering_attachment_accepter.tgw_peering_accepter.id
}
```

For accpeter, to allow connection to VPN connection and all VPCs, we will declare route to all vpc and on-premise. So, the default **transit_gateway_route_table** should be **cidr_block_allvpc** and **cidr_block_onpremise** target.