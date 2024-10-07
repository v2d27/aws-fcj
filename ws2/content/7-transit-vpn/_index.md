---
title : "Transit Gateway with VPN"
date :  "`r Sys.Date()`" 
weight : 7
chapter : false
pre : " <b> 7. </b> "
---


## I. VPN with VPG and TGW

#### 1. VPN Site-to-Site with Virtual Private Gateway (VPG)

When we establish a Site-to-Site VPN connection directly to a VPC, we must create a Virtual Private Gateway. We then attach this gateway to the VPC, and the VPC route tables will automatically propagate routing. We only need to **enable available propagation routing** for VPC. Please see [Create VPN Site-to-Site connection](https://v2d27.github.io/aws-fcj/ws1/4-sitetositevpn/4.3-createvpnconnection/) for more information.

#### 2. VPN Site-to-Site with Transit Gateway (TGW)

For establishing a Site-to-Site VPN connection with Transit Gateway, we will not create attachment because VPN connection is associated with a Transit Gateway automatically. But we have to only create static route on VPC route table. It will help VPC routing the direction to TGW. **Propagation routing is not available** in this connection. 

{{%notice note%}}
After successfully connection, please wait a short time in 3 or 5 minutes to communicate with each others in both of two sides.
{{%/notice%}}


## II. Creating TGW with VPN

To communicate with on-premise server, we only create one VPN connection from on-premise to AWS cloud, temporarily called Transit Gateway center. All other accounts and regions will connect through Transit Gateway Center.

![intro](/aws-fcj/ws2/images/2.content/transit-vpn.png)


Creating `transit-vpn.tf` file with the configurations below:

```terraform
# -------------------------------------------------------------------------------
# create vpn connection
# -------------------------------------------------------------------------------
# create customer gateway
resource "aws_customer_gateway" "cgw" {
    provider = aws.region_singapore
    # ASN of your on-premise network
    bgp_asn = 65000
    # Enter exactly your customer gate public IP address
    ip_address = aws_eip.on_premise.public_ip
    # Only support ipsec.1 now
    type = "ipsec.1"
}

# Make VPN connection from VPN to AWS Transit Gateway
resource "aws_vpn_connection" "transit_vpn" {
    provider = aws.region_singapore
    customer_gateway_id = aws_customer_gateway.cgw.id
    transit_gateway_id = aws_ec2_transit_gateway.my-tgw-1.id
    type = "ipsec.1"

    # use static route for vpn
    static_routes_only = true

    # limit ip range for vpn connection
    local_ipv4_network_cidr = var.cidr_block_onpremise
    remote_ipv4_network_cidr = var.cidr_block_allvpc
    
    # specific PSK tunnel1 and tunnel2 for VPN connection
    tunnel1_preshared_key = var.psk[0]
    tunnel2_preshared_key = var.psk[1]

    tags = {
        Name = "transit_vpn"
    }
} # => Please wait about 5 minutes after creation to ping successfully



# -------------------------------------------------------------------------------
# update transit_gateway_route table
# -------------------------------------------------------------------------------
resource "aws_ec2_transit_gateway_route" "tgw1_rt_route_vpn" {
    provider = aws.region_singapore
    # using default route table of transit gateway
    transit_gateway_route_table_id = aws_ec2_transit_gateway.my-tgw-1.association_default_route_table_id

    # aws_vpn_connection routing for transit gateway
    destination_cidr_block = var.cidr_block_onpremise
    transit_gateway_attachment_id = aws_vpn_connection.transit_vpn.transit_gateway_attachment_id
}



# -------------------------------------------------------------------------------
# update vpc route table
# -------------------------------------------------------------------------------
# update vpc1 route table for vpn connection
resource "aws_route" "vpc1_on_premise_route" {
    provider = aws.region_singapore
    route_table_id = aws_route_table.VPC1-RT-Public.id
    destination_cidr_block = local.cidr_on_premise # connect to on-premises
    transit_gateway_id = aws_ec2_transit_gateway.my-tgw-1.id
}

# update vpc2 route table for vpn connection
resource "aws_route" "vpc2_on_premise_route" {
    provider = aws.region_singapore
    route_table_id = aws_route_table.VPC2-RT-Private.id
    destination_cidr_block = local.cidr_on_premise # connect to on-premises
    transit_gateway_id = aws_ec2_transit_gateway.my-tgw-1.id
}

```


{{%notice info%}}
All arguments including **tunnel1_preshared_key** and **tunnel2_preshared_key** will be stored in the raw state as plain-text in Terraform.
{{%/notice%}}