#!/usr/bin/python

"""
- Author : Nag m
- Hack   : Get the bucket Policy
- Info   : Get the bucket policy
            * 101-s3-aws
"""

import boto
import json

def getpolicy(name):
   bucket = conn.get_bucket(name)
   bucket_policy =  bucket.get_policy()
   st = json.dumps(json.loads(bucket_policy),indent=4)
   print st

if __name__ == "__main__":
   conn = boto.connect_s3()
   bucketname = "101-s3-aws"
   getpolicy(bucketname)
