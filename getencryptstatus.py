#!/usr/bin/python

"""
- Author : Nag m
- Hack   : List whether the object is encrypted while at rest on the server
- Info   : List whether the object is encrypted while at rest on the server
            * 101-s3-aws
"""

import boto

def listobj(name):
   bucket = conn.get_bucket(name)
   lt =  bucket.list()
   for obj in lt:
       print obj.encrypted

if __name__ == "__main__":
   conn = boto.connect_s3()
   bucketname = "101-s3-aws"
   listobj(bucketname)
