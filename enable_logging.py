#!/usr/bin/python

"""
- Author : Nag m
- Hack   : Enable Logging for the S3 bucket
- Info   : Enable Logging for the S3 bucket
            * 101-s3-aws
"""

import boto

def logging(name):
   bucket = conn.get_bucket(name)
   log_bucket = conn.get_bucket("101bucket")
   log_bucket.set_as_logging_target()
   bucket.enable_logging(log_bucket)

if __name__ == "__main__":
   conn = boto.connect_s3()
   bucketname = "101-s3-aws"
   logging(bucketname)
