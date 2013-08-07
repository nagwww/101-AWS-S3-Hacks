#!/usr/bin/python

"""
- Author : Nag m
- Hack   : Generate a URL for the S3 bucket with an expiration time 20 seconds
- Info   : Generate a URL for the S3 bucket with an expiration time 20 seconds
            * 101-s3-aws
"""

import boto

def url(name):
   bucket = conn.get_bucket(name)
   print bucket.generate_url(20,"GET")

if __name__ == "__main__":
   conn = boto.connect_s3()
   bucketname = "101-s3-aws"
   url(bucketname)
