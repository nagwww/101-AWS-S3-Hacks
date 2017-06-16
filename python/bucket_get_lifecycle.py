#!/usr/bin/python

"""
- Hack   : Get the lifecycle policy of an S3 bucket
- AWS CLI: aws s3api get-bucket-lifecycle --bucket us-west-2.nag 
"""

import json
import boto3

if __name__ == "__main__":
    client = boto3.client('s3')
    bucketname = "us-west-2.nag"
    print client.get_bucket_lifecycle_configuration(Bucket=bucketname)
