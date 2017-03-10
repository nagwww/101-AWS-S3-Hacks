#!/usr/bin/python

"""
- Author : Nag m
- Hack   : Create an Bucket in S3
"""

import boto3

if __name__ == "__main__":
   client = boto3.client('s3')
   all_buckets =  client.list_buckets()["Buckets"]
   for bucket in all_buckets:
       print bucket["Name"], "Created on ", bucket["CreationDate"]
