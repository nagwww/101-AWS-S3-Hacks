#!/usr/bin/python

"""
- Author : Nag m
- Hack   : Delete bucket tagging
- AWS CLI: aws s3api delete-bucket-tagging --bucket us-west-2.nag
"""

import boto3

if __name__ == "__main__":
   client = boto3.client('s3')
   bucketname = "us-west-2.nag"
   print client.delete_bucket_tagging(Bucket=bucketname)
