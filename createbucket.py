#!/usr/bin/python

"""
- Author : Nag m
- Create a bucket named
  * 101-s3-aws
"""

import boto

def createabucket(name):
   bucket = conn.create_bucket(name)
   print "Bucket named ", bucket.name, " created"

if __name__ == "__main__":
   conn = boto.connect_s3()
   bucketname = "101-s3-aws"
   createabucket(bucketname)
