#!/usr/bin/python

"""
- Author : Nag m
- Hack   : Disable Logging for the S3 bucket
- Info   : Disable Logging for the S3 bucket
            * 101-s3-aws
"""

import boto

def logging(name):
   bucket = conn.get_bucket(name)
   bucket.disable_logging()

if __name__ == "__main__":
   conn = boto.connect_s3()
   bucketname = "101-s3-aws"
   logging(bucketname)
