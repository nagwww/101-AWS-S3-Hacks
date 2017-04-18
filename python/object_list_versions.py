#!/usr/bin/python

"""
- Author : Nag m
- Hack   : List all the versioned objects
- AWS CLI: aws s3api list-object-versions --bucket us-west-2.nag
"""

import json
import boto3

if __name__ == "__main__":
    client = boto3.client('s3')
    bucketname = "us-west-2.nag"
    print client.list_object_versions(Bucket=bucketname)
