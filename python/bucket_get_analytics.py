#!/usr/bin/python

"""
- Author : Nag m
- Hack   : Get the analytics configurations for an S3 bucket.
- AWS CLI: aws s3api get-bucket-analytics-configuration --bucket us-west-2.nag --id full
"""

import boto3

if __name__ == "__main__":
    client = boto3.client('s3')
    bucketname = "us-west-2.nag"
    analytics_config = client.get_bucket_analytics_configuration(Bucket=bucketname, Id="full")
    print analytics_config["AnalyticsConfiguration"]
