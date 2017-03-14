#!/usr/bin/python

"""
- Author : Nag m
- Hack   : Create an Object in S3
- AWS CLI: aws s3 ls s3://us-west-2.nag
"""

import json
import boto3

if __name__ == "__main__":
    client = boto3.client('s3', region_name="us-west-2")
    bucketname = "us-west-2.nag"
    for obj in client.list_objects(Bucket=bucketname)["Contents"]:
        print obj["Key"]
