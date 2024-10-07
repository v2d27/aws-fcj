---
title : "VPC Peering in Terraform"
date : "`r Sys.Date()`"
weight : 1
chapter : false
pre : " <b> 5.1 </b> "
---


#### VPC Peering intra-region

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

If you want to enable private DNS resolution for vpc_peering:
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



#### VPC Peering inter-region or cross-account

For cross-account (requester's AWS account differs from the accepter's AWS account) or inter-region VPC Peering Connections use the **aws_vpc_peering_connection** resource to manage the requester's side of the connection and use the **aws_vpc_peering_connection_accepter** resource to manage the accepter's side of the connection.

Terraform VPC Peering inter-region between VPC1 and VPC2 example:

![intro](/aws-fcj/ws2/images/2.content/vpc-peering-inter-region.png)

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

If you want to enable DNS resolution for inter-region or cross-account, change options of connection:

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


