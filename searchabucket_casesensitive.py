#!/usr/bin/python

"""
- Author : Nag m
- Search for a bucket named
  * 101-s3-aws
"""

import boto
from boto.s3.connection import OrdinaryCallingFormat

def searchabucket():
   bucket = conn.get_bucket("101-S3-aws")
   print bucket

if __name__ == "__main__":
   conn = boto.connect_s3(calling_format=OrdinaryCallingFormat())
   searchabucket()
