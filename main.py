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

statuses = ec2_client.describe_instance_status()
for status in statuses['InstanceStatuses']:
    ins_status = status["InstanceState"]["Name"]
    sys_status = status["SystemStatus"]["Status"]
    state = status["InstanceState"]["Name"]
    print(f"Instance {status['InstanceId']} is {state} is {ins_status} and system status is {sys_status}")
