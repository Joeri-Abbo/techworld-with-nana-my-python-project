import boto3

region = 'eu-west-3'
ec2_client = boto3.client(
    'ec2',
    region_name=region
)
ec2_resource = boto3.resource(
    'ec2',
    region_name=region
)

instances = ec2_client.describe_instances()

for reservation in instances['Reservations']:
    instances = reservation["Instances"]
    for instance in instances:
        print(f"Instance {instance['InstanceId']} is {instance['State']['Name']}")

statuses = ec2_client.describe_instance_status()
for status in statuses['InstanceStatuses']:
    ins_status = status["InstanceState"]["Name"]
    sys_status = status["SystemStatus"]["Status"]
    print(f"Instance {status['InstanceId']} is {ins_status} and system status is {sys_status}")