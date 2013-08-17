#!/usr/bin/python

"""
- Author : Nag m
- Hack   : Add a tag to S3 bucket
- Info   : Add a tag to S3 bucket
            * 101-s3-aws
"""

import boto

def lifecycle(name):
   bucket = conn.get_bucket(name)
   tag = bucket.get_tags()
   print tag

if __name__ == "__main__":
   conn = boto.connect_s3()
   bucketname = "101-s3-aws"
   lifecycle(bucketname)
