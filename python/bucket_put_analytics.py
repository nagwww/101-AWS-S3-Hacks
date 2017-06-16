#!/usr/bin/python

"""
- Author : Nag m
- Hack   : Create analytics configurations for an S3 bucket.
- AWS CLI: aws s3api put-bucket-analytics-configuration --bucket us-west-2.nag --analytics-configuration '{"Id": "full1","StorageClassAnalysis": {}}' --id "full1"
"""

import boto3

config = {"Id": "full1","StorageClassAnalysis": {}}

if __name__ == "__main__":
    client = boto3.client('s3')
    bucketname = "us-west-2.nag"
    analytics_config = client.put_bucket_analytics_configuration(Bucket=bucketname, Id="full1", AnalyticsConfiguration=config)
    print analytics_config
