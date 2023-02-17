import boto3
from operator import itemgetter

region = 'eu-west-3'
ec2_client = boto3.client(
    'ec2',
    region_name=region
)

volumes = ec2_client.describe_volumes(
    Filters=[
        {
            'Name': 'tag:Name',
            "Values": [
                "prod"
            ]
        }
    ]
)

for volume in volumes['Volumes']:

    snapshots = ec2_client.describe_snapshots(
        OwnerIds=['self'],
        Filters=[
            {
                'Name': 'volume-id',
                'Values': [volume['VolumeId']]
            }
        ]
    )
    sorted_by_date = sorted(
        snapshots['Snapshots'],
        key=itemgetter('StartTime'),
        reverse=True
    )
    #
    # for snapshot in snapshots['Snapshots']:
    #     print(snapshot['StartTime'])
    #
    # print("-" * 50)
    # for snapshot in sorted_by_date:
    #     print(snapshot['StartTime'])
    for snapshot in sorted_by_date[2:]:
        response = ec2_client.delete_snapshot(
            SnapshotId=snapshot['SnapshotId']
        )
        print(response)
