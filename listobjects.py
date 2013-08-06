#!/usr/bin/python

"""
- Author : Nag m
- Hack   : List all the objects with in a bucket
- Info   : List all the objects with in a bucket
            * 101-s3-aws
"""

import boto

def listobj(name):
   bucket = conn.get_bucket(name)
   lt =  bucket.list()
   for obj in lt:
       print obj.name

if __name__ == "__main__":
   conn = boto.connect_s3()
   bucketname = "101-s3-aws"
   listobj(bucketname)
