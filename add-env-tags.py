import boto3

region = 'eu-west-3'
ec2_client_paris = boto3.client(
    'ec2',
    region_name=region
)
ec2_resource_paris = boto3.resource(
    'ec2',
    region_name=region
)

instance_ids_paris = []
reservation_paris = ec2_client_paris.describe_instances()['Reservations']
for res in reservation_paris:
    instances = res['Instances']
    for instance in instances:
        instance_ids_paris.append(instance['InstanceId'])

response = ec2_resource_paris.create_tags(
    Resources=instance_ids_paris,
    Tags=[
        {
            'Key': 'environment',
            'Value': 'prod'
        }
    ]
)

print(response)
