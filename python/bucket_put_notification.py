#!/usr/bin/python

"""
- Hack   : Create a SQS notification
- AWS CLI: aws s3api put-bucket-notification-configuration --bucket us-west-2.nag --notification-configuration   file://./notification.json
- Issue : Get-get-notification returns QueueConfiguration instead of QueueConfigurations
"""

import json
import boto3

p = {
    "QueueConfigurations": {
        "QueueArn": "arn:aws:sqs:us-west-2:220580744359:nag1",
        "Events": [
            "s3:ObjectCreated:Post"
        ],
        "Id": "MjcwMTRjOGUtZDVkYS00YTA3LThkMTgtNTEwNmI3OTExNzBi",
        "Event": "s3:ObjectCreated:Post"
    }
}

if __name__ == "__main__":
    client = boto3.client('s3')
    bucketname = "us-west-2.nag"
    print client.put_bucket_notification_configuration(Bucket=bucketname, NotificationConfiguration=p)
