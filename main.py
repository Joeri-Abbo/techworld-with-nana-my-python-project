import boto3

client = boto3.client(
    'ec2',
    # region_name='us-east-1'
)
all_availability_vpcs = client.describe_vpcs()
vpcs = all_availability_vpcs["Vpcs"]

for vpc in vpcs:
    print(vpc["VpcId"])
    cidr_block_association_set = vpc["CidrBlockAssociationSet"]
    for cidr_block_association in cidr_block_association_set:
        print(cidr_block_association["CidrBlockState"])
