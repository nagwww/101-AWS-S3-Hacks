#!/usr/bin/python

"""
- Author : Nag m
- Hack   : Delete a bucket policy
- AWS CLI: aws s3api get-bucket-policy --bucket us-west-2.nag
"""

import json
import boto3

if __name__ == "__main__":
    client = boto3.client('s3')
    bucketname = "us-west-2.nag"
    print client.get_bucket_policy(Bucket=bucketname)["Policy"]
