from operator import itemgetter

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

instance_id = 'i-02078856a347e1079'

volumes = ec2_client.describe_volumes(
    Filters=[
        {
            'Name': 'attachment.instance-id',
            'Values': [instance_id]}
    ]
)
instance_volume = volumes['Volumes'][0]

snapshots = ec2_client.describe_snapshots(
    OwnerIds=['self'],
    Filters=[
        {
            'Name': 'volume-id',
            'Values': [instance_volume['VolumeId']]
        }
    ]
)
latest_snapshot = sorted(
    snapshots['Snapshots'],
    key=itemgetter('StartTime'),
    reverse=True
)[0]

new_volume = ec2_client.create_volume(
    SnapshotId=latest_snapshot["SnapshotId"],
    AvailabilityZone=instance_volume["AvailabilityZone"],
    TagSpecifications=[
        {
            'ResourceType': 'volume',
            'Tags': [
                {
                    'Key': 'Name',
                    'Value': 'prod'
                },
            ]
        },
    ]
)
while True:
    volume_status = ec2_client.describe_volumes(
        VolumeIds=[new_volume["VolumeId"]]
    )
    print(volume_status["Volumes"][0]["State"])
    if volume_status["Volumes"][0]["State"] == "available":
        print(volume_status["Volumes"][0]["State"])
        ec2_resource.Instance(instance_id).attach_volume(
            Device='/dev/xvdb',
            VolumeId=new_volume["VolumeId"]
        )
        break
