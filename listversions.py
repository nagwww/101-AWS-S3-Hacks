#!/usr/bin/python

"""
- Author : Nag m
- Hack   : List all the objects with the versions for a given Bucket
- Info   : List all the objects with the versions for a given bucket
            * 101-s3-aws
"""

import boto

def listversions(name):
   bucket = conn.get_bucket(name)
   lt = bucket.list_versions()
   print lt
   for name in lt:
       print name.name

if __name__ == "__main__":
   conn = boto.connect_s3()
   bucketname = "101-s3-aws"
   listversions(bucketname)
