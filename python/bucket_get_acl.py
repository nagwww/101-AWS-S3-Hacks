#!/usr/bin/python

"""
- Author : Nag m
- Hack   : Get an ACL for a bucket
- AWS CLI: aws s3api get-bucket-acl --bucket us-west-2.nag
"""

import json
import boto3

if __name__ == "__main__":
    client = boto3.client('s3')
    bucketname = "us-west-2.nag"
    print json.dumps(client.get_bucket_acl(Bucket=bucketname)["Grants"], indent=1)
