#!/usr/bin/python

"""
- Author : Nag m
- Hack   : Get lifecycle to S3 bucket as xml
- Info   : Get lifecycle to S3 bucket as xml
            * 101-s3-aws
"""

import boto

def lifecycle(name):
   bucket = conn.get_bucket(name)
   lifecycle = bucket.get_lifecycle_config()
   print lifecycle.to_xml()

if __name__ == "__main__":
   conn = boto.connect_s3()
   bucketname = "101bucket"
   lifecycle(bucketname)
