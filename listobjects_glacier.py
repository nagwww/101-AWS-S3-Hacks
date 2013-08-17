#!/usr/bin/python

"""
- Author : Nag m
- Hack   : List all the objects with in a bucket and if the object is moved to Glacier
- Info   : List all the objects with in a bucket. When an object transitions to Glacier, the storage class will be updated
            * 101-s3-aws
"""

import boto

def listobj(name):
   bucket = conn.get_bucket(name)
   lt =  bucket.list()
   for obj in lt:
       print obj.name, obj.storage_class

if __name__ == "__main__":
   conn = boto.connect_s3()
   bucketname = "101-s3-aws"
   listobj(bucketname)
