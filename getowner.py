#!/usr/bin/python

"""
- Author : Nag m
- Hack   : List all the objects Owner
- Info   : List all the objects Owner
            * 101-s3-aws
"""

import boto

def listobj(name):
   bucket = conn.get_bucket(name)
   lt =  bucket.list()
   for obj in lt:
       print obj.owner.id
       print obj.owner.display_name

if __name__ == "__main__":
   conn = boto.connect_s3()
   bucketname = "com."
   listobj(bucketname)
