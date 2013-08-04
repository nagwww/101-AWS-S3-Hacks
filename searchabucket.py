#!/usr/bin/python

"""
- Author : Nag m
- Hack   : Search for a specific bucket
- Info   : Search for a bucket named
  	   * 101-s3-aws
"""

import boto

def searchabucket():
   bucket = conn.lookup("101-s3-aws")
   print bucket.name

if __name__ == "__main__":
   conn = boto.connect_s3()
   searchabucket()
