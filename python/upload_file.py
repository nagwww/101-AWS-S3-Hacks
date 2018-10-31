#!/usr/bin/python

"""
- Author : Nag m
- Hack   : Upload a file to S3
- AWS CLI: aws s3api put-object --bucket us-west-2.nag --key hello.txt --body hello.txt
"""

import boto3

if __name__ == "__main__":
    client = boto3.client('s3', region_name="us-west-2")
    bucket_name = "us-west-2.nag"
    print client.upload_file(Bucket=bucket_name, Key="hello.txt", Filename="hello.txt")
