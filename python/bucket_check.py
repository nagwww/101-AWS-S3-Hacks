#!/usr/bin/python

"""
- Author : Nag m
- Hack   : Check if a bucket is present and can access it
- AWC CLI: aws s3api head-bucket --bucket us-west-2.nag
"""

import boto3

if __name__ == "__main__":
    client = boto3.client('s3')
    bucket_name = "us-west-2.nag"
    print client.head_bucket(Bucket=bucket_name)
