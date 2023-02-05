import boto3
import schedule

region = 'eu-west-3'
ec2_client = boto3.client(
    'ec2',
    region_name=region
)
ec2_resource = boto3.resource(
    'ec2',
    region_name=region
)


def check_instance_status():
    statuses = ec2_client.describe_instance_status(
        IncludeAllInstances=True,
    )
    for status in statuses['InstanceStatuses']:
        ins_status = status["InstanceState"]["Name"]
        sys_status = status["SystemStatus"]["Status"]
        state = status["InstanceState"]["Name"]
        print(f"Instance {status['InstanceId']} is {state} is {ins_status} and system status is {sys_status}")
    print("-" * 50)


schedule.every(5).seconds.do(check_instance_status)

while True:
    schedule.run_pending()
