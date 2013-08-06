#!/usr/bin/python

"""
- Author : Nag m
- Hack   : Disable a buckets Versioning 
- Info   : Disable a buckets Versioning
            * 101-s3-aws
"""

import boto

def addacl(name):
   bucket = conn.get_bucket(name)
   print bucket.configure_versioning(False)

if __name__ == "__main__":
   conn = boto.connect_s3()
   bucketname = "101-s3-aws"
   addacl(bucketname)
