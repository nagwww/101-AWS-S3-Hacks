#!/usr/bin/python

"""
- Author  : Nag m
- Hack    : Create an Bucket in S3
- AWS CLI : aws s3api create-bucket  --bucket us-east-1.nag
"""

import boto3

if __name__ == "__main__":
    client = boto3.client('s3')
    bucketname = "us-east-1.nag"
    print client.create_bucket(Bucket=bucketname)
