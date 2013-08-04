#!/usr/bin/python

"""
- Author : Nag m
- Hack   : Search for a bucket with bucket name which is case sensitive
- Info   : Search for a bucket named
 	 * 101-S3-aws
"""

import boto
from boto.s3.connection import OrdinaryCallingFormat

def searchabucket():
   bucket = conn.get_bucket("101-S3-aws")
   print bucket

if __name__ == "__main__":
   conn = boto.connect_s3(calling_format=OrdinaryCallingFormat())
   searchabucket()
