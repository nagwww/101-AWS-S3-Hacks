#!/usr/bin/python

"""
- Author : Nag m
- Hack   : Delete object tagging
- AWS CLI: aws s3api delete-object-tagging --bucket us-west-2.nag --key hello.txt
"""

import boto3

if __name__ == "__main__":
    client = boto3.client('s3')
    bucketname = "us-west-2.nag"
    print client.delete_object_tagging(Bucket=bucketname, Key="hello.txt")
