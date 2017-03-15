#!/usr/bin/python

"""
- Author : Nag m
- Hack   : Get all the tags for an S3 object
- AWS CLI: aws s3api get-object-tagging --bucket us-west-2.nag --key hello.txt
"""

import boto3

if __name__ == "__main__":
    client = boto3.client('s3')
    bucketname = "us-west-2.nag"
    print client.get_object_tagging(Bucket=bucketname, Key="hello.txt")["TagSet"]
