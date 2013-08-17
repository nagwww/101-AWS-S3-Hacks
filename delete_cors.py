#!/usr/bin/python

"""
- Author : Nag m
- Hack   : Delete all cors for the s3 bucket
- Info   : Delete all cors for the s3 bucket
            * 101-s3-aws
"""

import boto

def lifecycle(name):
   bucket = conn.get_bucket(name)
   bucket.delete_cors()

if __name__ == "__main__":
   conn = boto.connect_s3()
   bucketname = "101-s3-aws"
   lifecycle(bucketname)
