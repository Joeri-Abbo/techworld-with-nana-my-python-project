import boto3

region = 'us-west-3'
ec2_client = boto3.client(
    'ec2',
    region_name=region
)
ec2_resource = boto3.resource(
    'ec2',
    region_name=region
)

new_vpc = ec2_resource.create_vpc(
    CidrBlock='10.0.0.0/16',
)

new_vpc.create_subnet(
    CidrBlock='10.0.1.0/24',
)

new_vpc.create_subnet(
    CidrBlock='10.0.2.0/24',
)

new_vpc.create_tags(
    Tags=[
        {
            "Key": "Name",
            "Value": "my-vpc"
        }
    ]
)

all_availability_vpcs = ec2_client.describe_vpcs()
vpcs = all_availability_vpcs["Vpcs"]

for vpc in vpcs:
    print(vpc["VpcId"])
    cidr_block_association_set = vpc["CidrBlockAssociationSet"]
    for cidr_block_association in cidr_block_association_set:
        print(cidr_block_association["CidrBlockState"])
