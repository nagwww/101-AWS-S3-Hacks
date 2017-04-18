#!/usr/bin/python

"""
- Author : Nag m
- Hack   : List all the versioned objects
- AWS CLI: aws s3api list-object-versions --bucket us-west-2.nag --prefix hello.txt
"""

import json
import boto3

if __name__ == "__main__":
    client = boto3.client('s3')
    bucketname = "us-west-2.nag"
    all_versions = client.list_object_versions(Bucket=bucketname, Prefix="hello.txt")["Versions"]
    for obj in all_versions:
        print "Last modified, isLatest, size => ", obj["LastModified"], obj["IsLatest"], obj["Size"]
