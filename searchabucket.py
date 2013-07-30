#!/usr/bin/python

"""
- Author : Nag m
- Search for a bucket named
  * 101-s3-aws
- Did you know that lookup is case insensitive  
"""

import boto

def searchabucket():
   bucket = conn.lookup("101-s3-aws")
   print bucket.name

if __name__ == "__main__":
   conn = boto.connect_s3()
   searchabucket()
