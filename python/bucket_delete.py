#!/usr/bin/python

"""
- Author : Nag m
- Hack   : Delete an Bucket in S3
"""

import boto3

if __name__ == "__main__":
   client = boto3.client('s3')
   bucket_name = "101-s3-aws-1"
   print client.delete_bucket(Bucket=bucket_name)
