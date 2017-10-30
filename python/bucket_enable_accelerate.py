#!/usr/bin/python

"""
- Author : Nag m
- Hack   : Enable bucket acceleration ( FYI : Bucket names containing a period cannot be enabled for acceleration )
"""

import boto3

if __name__ == "__main__":
    client = boto3.client('s3')
    bucket_name = "us-west-2-nag"
    print client.put_bucket_accelerate_configuration(Bucket=bucket_name, AccelerateConfiguration={'Status': 'Enabled'})
