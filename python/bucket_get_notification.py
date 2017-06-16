#!/usr/bin/python

"""
- Hack   : Get the S3 bucket notification
- AWS CLI: aws s3api get-bucket-notification --bucket us-west-2.nag
"""

import json
import boto3

if __name__ == "__main__":
    client = boto3.client('s3')
    bucketname = "us-west-2.nag"
    print client.get_bucket_notification_configuration(Bucket=bucketname)
