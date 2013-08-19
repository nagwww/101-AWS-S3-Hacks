#!/usr/bin/python

"""
- Author : Nag m
- Hack   : Disable  buckets Versioning 
- Info   : Disable  buckets Versioning
            * 101-s3-aws
"""

import boto

def disable(name):
   bucket = conn.get_bucket(name)
   print bucket.configure_versioning(False)

if __name__ == "__main__":
   conn = boto.connect_s3()
   bucketname = "101-s3-aws"
   disable(bucketname)
