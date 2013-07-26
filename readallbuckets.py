#!/usr/bin/python

"""
- Author : Nag m
- Lists all the buckets 
"""

import boto

def getallbuckets():
   buckets = conn.get_all_buckets()
   for b in buckets:
       print b.name

if __name__ == "__main__":
   conn = boto.connect_s3()
   getallbuckets()
