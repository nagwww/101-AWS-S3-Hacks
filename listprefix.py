#!/usr/bin/python

"""
- Author : Nag m
- Hack   : List all the objects with in a bucket with a prefix
- Info   : List all the objects with in a bucket with a prefix
            * 101-s3-aws
"""

import boto

def listobj(name):
   bucket = conn.get_bucket(name)
   bucketListResultSet = bucket.list(prefix="folder")
   for key in bucketListResultSet:
       print key.name

if __name__ == "__main__":
   conn = boto.connect_s3()
   bucketname = "101-s3-aws"
   listobj(bucketname)
