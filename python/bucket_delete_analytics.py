#!/usr/bin/python

"""
- Author : Nag m
- Hack   : Delete analytics configurations for an S3 bucket.
- AWS CLI: aws s3api delete-bucket-analytics-configuration --bucket us-west-2.nag --id full1
"""

import boto3

if __name__ == "__main__":
    client = boto3.client('s3')
    bucketname = "us-west-2.nag"
    analytics_config = client.delete_bucket_analytics_configuration(Bucket=bucketname, Id="full1")
    print analytics_config
