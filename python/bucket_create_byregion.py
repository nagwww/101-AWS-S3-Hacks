#!/usr/bin/python

"""
- Author : Nag m
- Hack   : Create an Bucket in S3
"""

import boto3

if __name__ == "__main__":
   client = boto3.client('s3')
   bucketname = "eu-west-1.nag1"
   print client.create_bucket(Bucket=bucketname, CreateBucketConfiguration={ 'LocationConstraint': 'us-west-1' })
