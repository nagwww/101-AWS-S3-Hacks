#!/usr/bin/python

"""
- Author : Nag m
- Hack   : Delete lifecycle to S3 bucket
- Info   : Delete lifecycle to S3 bucket
            * 101-s3-aws
"""

import boto

def lifecycle(name):
   bucket = conn.get_bucket(name)
   print bucket.delete_lifecycle_configuration()

if __name__ == "__main__":
   conn = boto.connect_s3()
   bucketname = "101bucket"
   lifecycle(bucketname)
