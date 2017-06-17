#!/usr/bin/python

"""
- Author : Nag m
- Hack   : List all the S3 buckets in an account
- AWS CLI: aws s3 ls
"""

import boto3

if __name__ == "__main__":
    client = boto3.client('s3')
    all_buckets = client.list_buckets()["Buckets"]
    for bucket in all_buckets:
        print bucket["Name"], "Created on ", bucket["CreationDate"]
