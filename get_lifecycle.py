#!/usr/bin/python

"""
- Author : Nag m
- Hack   : Get lifecycle to S3 bucket
- Info   : Get lifecycle to S3 bucket
            * 101-s3-aws
"""

import boto

def lifecycle(name):
   bucket = conn.get_bucket(name)
   lifecycle = bucket.get_lifecycle_config()
   for rule in lifecycle:
       print rule.id
       print rule.expiration.days
       print rule.expiration.date
       print rule.transition
       print rule.prefix

if __name__ == "__main__":
   conn = boto.connect_s3()
   bucketname = "101bucket"
   lifecycle(bucketname)
