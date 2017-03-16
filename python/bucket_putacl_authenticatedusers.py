#!/usr/bin/python

"""
- Author : Nag m
- Hack   : Grant read access to Authenticated users ( You sure don't want to do this anytime )
- AWS CLI:aws s3api put-bucket-acl --bucket us-west-2.nag --grant-read uri=http://acs.amazonaws.com/groups/global/AuthenticatedUsers
"""

import json
import boto3

if __name__ == "__main__":
    client = boto3.client('s3')
    bucketname = "us-west-2.nag"
    print client.put_bucket_acl(Bucket=bucketname, ACL="authenticated-read")
