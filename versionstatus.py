#!/usr/bin/python

"""
- Author : Nag m
- Hack   : Find out the status of the Bucket Versioning 
- Info   : Find out the status of the Bucket Versioning
            * 101-s3-aws
"""

import boto

def version(name):
   bucket = conn.get_bucket(name)
   print bucket.get_versioning_status()

if __name__ == "__main__":
   conn = boto.connect_s3()
   bucketname = "101-s3-aws"
   version(bucketname)
