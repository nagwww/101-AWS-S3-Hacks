#!/usr/bin/python

"""
- Author : Nag m
- Hack   : Make S3 bucket public readable
- Info   : Make S3 bucket public readable
            * 101-s3-aws
"""

import boto

def makepublic(name):
   bucket = conn.get_bucket(name)
   bucket.make_public()

if __name__ == "__main__":
   conn = boto.connect_s3()
   bucketname = "101-s3-aws"
   makepublic(bucketname)
