#!/usr/bin/python

"""
- Author : Nag m
- Hack   : Get all the versions of the S3 Objects
- Info   : Get all the versions of the S3 Objects
            * 101-s3-aws
"""

import boto

def version(name):
   bucket = conn.get_bucket(name)
   for name in bucket.get_all_versions():
       print name

if __name__ == "__main__":
   conn = boto.connect_s3()
   bucketname = "101-s3-aws"
   version(bucketname)
