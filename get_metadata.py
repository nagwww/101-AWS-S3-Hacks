#!/usr/bin/python

"""
- Author : Nag m
- Hack   : Get all the metadata added to the S3 object
- Info   : Get all the metadata added to the S3 object
            * 101-s3-aws
"""

import boto

def listobj(name):
   bucket = conn.get_bucket(name)
   key = bucket.lookup("myfile1.txt")
   print key.metadata

if __name__ == "__main__":
   conn = boto.connect_s3()
   bucketname = "101-s3-aws"
   listobj(bucketname)
