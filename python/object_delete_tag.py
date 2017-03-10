#!/usr/bin/python

"""
- Author : Nag m
- Hack   : Create an Object in S3
"""

import json
import boto3

if __name__ == "__main__":
   client = boto3.client('s3')
   bucketname = "101-s3-aws"
   print client.delete_object_tagging(Bucket=bucketname, Key="hello.txt")
