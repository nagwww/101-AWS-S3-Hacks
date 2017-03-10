#!/usr/bin/python

"""
- Author : Nag m
- Hack   : Delete an Bucket in S3
"""

import boto3

if __name__ == "__main__":
   client = boto3.client('s3',region_name="eu-west-1")
   bucket_name = "eu-west-1.nag"
   print client.delete_bucket(Bucket=bucket_name)
