#!/usr/bin/python

"""
- Author : Nag m
- Hack   : Create bucket policy
- AWS CLI: aws s3api put-bucket-policy --bucket us-west-2.nag --policy '{"Version":"2012-10-17","Statement":[{"Sid":"AddPerm","Effect":"Allow","Principal":"*","Action":"s3:GetObject","Resource":"arn:aws:s3:::us-west-2.nag/*"}]}'
"""

import json
import boto3

p = {"Version": "2012-10-17", "Statement": [
    {"Sid": "AddPerm", "Effect": "Allow", "Principal": "*", "Action": "s3:GetObject",
     "Resource": "arn:aws:s3:::us-west-2.nag/*"}]}

if __name__ == "__main__":
    client = boto3.client('s3')
    bucketname = "us-west-2.nag"
    print client.put_bucket_policy(Bucket=bucketname, Policy=json.dumps(p))
