#!/usr/bin/python

"""
- Author : Nag m
- Hack   : Set the bucket Policy
- Info   : Set the bucket policy
            * 101-s3-aws
"""

import boto
import json
policy = '{ "Version": "2008-10-17", "Id": "Policy1375842722283", "Statement": [ { "Action": "s3:list*", "Principal": { "AWS": "*" }, "Resource": "arn:aws:s3:::101-s3-aws", "Effect": "Allow", "Sid": "Stmt1375842721085" } ] }'

def setpolicy(name):
   bucket = conn.get_bucket(name)
   bucket_policy =  bucket.set_policy(policy)

if __name__ == "__main__":
   conn = boto.connect_s3()
   bucketname = "101-s3-aws"
   setpolicy(bucketname)
