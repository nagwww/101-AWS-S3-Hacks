#!/usr/bin/python

"""
- Author : Nag m
- Hack   : Delete tags of a S3 bucket
- Info   : Delete tags of a S3 bucket
            * 101-s3-aws
"""

import boto

def tags(name):
   bucket = conn.get_bucket(name)
   print bucket.delete_tags()

if __name__ == "__main__":
   conn = boto.connect_s3()
   bucketname = "101-s3-aws"
   tags(bucketname)
