#!/usr/bin/python

"""
- Author : Nag m
- Hack   : Lists the analytics configurations for an S3 bucket.
- AWS CLI: aws s3api list-bucket-analytics-configurations --bucket us-west-2.nag
"""

import boto3

if __name__ == "__main__":
    client = boto3.client('s3')
    bucketname = "us-west-2.nag"
    analytics_config = client.list_bucket_analytics_configurations(Bucket=bucketname)
    print analytics_config["AnalyticsConfigurationList"]
