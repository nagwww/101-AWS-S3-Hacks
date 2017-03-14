#!/usr/bin/python

"""
- Author : Nag m
- Hack   : Delete an Bucket in S3
- AWS CLI: aws s3api delete-bucket --bucket us-east-1.nag
"""

import boto3

if __name__ == "__main__":
    client = boto3.client('s3')
    bucket_name = "us-east-1.nag"
    print client.delete_bucket(Bucket=bucket_name)
