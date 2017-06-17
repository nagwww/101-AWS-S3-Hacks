#!/usr/bin/python

"""
- Author : Nag m
- Hack   : Suspend versioning for an S3 bucket
- AWS CLI: aws s3api put-bucket-versioning --bucket us-west-2.nag --versioning-configuration '{"Status":"Suspended"}'
"""

import json
import boto3

v = {
    'Status': 'Suspended'
}

if __name__ == "__main__":
    client = boto3.client('s3')
    bucketname = "us-west-2.nag"
    print client.put_bucket_versioning(Bucket=bucketname, VersioningConfiguration=v)
