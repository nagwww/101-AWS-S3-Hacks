#!/usr/bin/python2.7

"""
- Author : Nag m
- Hack   : Delete all objects in a bucket
- Info   : Delete all objects in a bucket
            * 101-s3-aws
"""

import boto
from boto.s3.connection import OrdinaryCallingFormat

def deleteall(name):
   bucket = conn.get_bucket(name)
   for obj in bucket.list():
       print " Deleting ... ", obj.name, obj.delete()

if __name__ == "__main__":
   conn = boto.connect_s3(calling_format=OrdinaryCallingFormat())
   bucketname = "101-s3-aws"
   deleteall(bucketname)
