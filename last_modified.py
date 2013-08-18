#!/usr/bin/python

"""
- Author : Nag m
- Hack   : List all the objects last modified timestamp in Zulu format
- Info   : List all the objects last modified timestamp in Zulu format
            * 101-s3-aws
"""

import boto

def modified(name):
   bucket = conn.get_bucket(name)
   lt =  bucket.list()
   for obj in lt:
       print obj.last_modified

if __name__ == "__main__":
   conn = boto.connect_s3()
   bucketname = "101-s3-aws"
   modified(bucketname)
