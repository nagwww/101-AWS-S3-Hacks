#!/usr/bin/python

"""
- Author : Nag m
- Hack   : Get all the tags for an S3 bucket
- AWC CLI: aws s3api get-bucket-tagging --bucket us-west-2.nag
"""

import boto3

if __name__ == "__main__":
    client = boto3.client('s3')
    bucketname = "us-west-2.nag"
    print client.get_bucket_tagging(Bucket=bucketname)["TagSet"]
