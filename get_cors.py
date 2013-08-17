#!/usr/bin/python

"""
- Author : Nag m
- Hack   : Get CORS for an S3 bucket
- Info   : Get CORS for an S3 bucket
            * 101-s3-aws
"""

import boto

def cors(name):
   bucket = conn.get_bucket(name)
   cors = bucket.get_cors()
   print cors

if __name__ == "__main__":
   conn = boto.connect_s3()
   bucketname = "101-s3-aws"
   cors(bucketname)
