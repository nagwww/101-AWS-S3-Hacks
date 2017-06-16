#!/usr/bin/python

"""
- Hack   : Delete website configuration for an S3 bucket
- AWS CLI: aws s3api delete-bucket-website --bucket us-west-2.nag
"""

import json
import boto3

if __name__ == "__main__":
    client = boto3.client('s3')
    bucketname = "us-west-2.nag"
    print client.delete_bucket_website(Bucket=bucketname)
