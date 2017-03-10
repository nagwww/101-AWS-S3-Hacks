#!/usr/bin/python

"""
- Author : Nag m
- Hack   : Delete an Bucket in S3
- AWS CLI: aws s3api delete-bucket --bucket us-west-1.nag ( You do not have to specify the region when deleting the bucket )
"""

import boto3

if __name__ == "__main__":
    client = boto3.client('s3', region_name="us-west-1")
    bucket_name = "us-west-1.nag"
    print client.delete_bucket(Bucket=bucket_name)
