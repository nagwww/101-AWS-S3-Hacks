#!/usr/bin/python

"""
- Author : Nag m
- Hack   : Delete an Object in S3
"""

import boto3

if __name__ == "__main__":
   client = boto3.client('s3')
   bucketname = "101-s3-aws"
   print client.delete_object(Bucket=bucketname, Key="hello.txt")
