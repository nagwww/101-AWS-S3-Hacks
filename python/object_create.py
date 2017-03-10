#!/usr/bin/python

"""
- Author : Nag m
- Hack   : Create an Object in S3
"""

import boto3

if __name__ == "__main__":
   client = boto3.client('s3',region_name="us-west-2")
#   bucketname = "101-s3-aws"
   bucketname = "us-west-2.nag"
   print client.put_object(Bucket=bucketname, Key="hello.txt", Body="Hello World")
