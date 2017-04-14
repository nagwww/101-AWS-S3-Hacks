#!/usr/bin/python

"""
- Author : Nag m
- Hack   : Get versioning for an S3 bucket
- AWS CLI: aws s3api get-bucket-versioning --bucket us-west-2.nag 
"""

import json
import boto3

v = {
    'Status': 'Enabled'
}

if __name__ == "__main__":
    client = boto3.client('s3')
    bucketname = "us-west-2.nag"
    print client.get_bucket_versioning(Bucket=bucketname)
