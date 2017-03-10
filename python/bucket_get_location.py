#!/usr/bin/python

"""
- Author : Nag m
- Hack   : Create an Bucket in S3
"""

import boto3

if __name__ == "__main__":
   client = boto3.client('s3')
   bucketname = "us-west-2.nag"
   print client.get_bucket_location(Bucket=bucketname)["LocationConstraint"]
