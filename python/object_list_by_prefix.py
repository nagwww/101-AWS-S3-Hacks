#!/usr/bin/python

"""
- Author : Nag m
- Hack   : Create an Object in S3
"""

import json
import boto3

if __name__ == "__main__":
   client = boto3.client('s3',region_name="us-west-2")
   bucketname = "us-west-2.nag"
   for obj in client.list_objects(Bucket=bucketname, Prefix="AWSLogs/")["Contents"]:
       print obj["Key"]
