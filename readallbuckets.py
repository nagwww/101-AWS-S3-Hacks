#!/usr/bin/python

"""
- Author : Nag m
- Hack   : List all the S3 buckets
- Info   : List all the buckets 
"""

import boto

def getallbuckets():
   buckets = conn.get_all_buckets()
   for b in buckets:
       print b.name, "\t", b.creation_date

if __name__ == "__main__":
   conn = boto.connect_s3()
   getallbuckets()
