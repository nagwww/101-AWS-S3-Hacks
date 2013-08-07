#!/usr/bin/python

"""
- Author : Nag m
- Hack   : List all the grants for a given Bucket
- Info   : List all the grants for a given bucket
            * 101-s3-aws
"""

import boto

def listgrants(name):
   bucket = conn.get_bucket(name)
   lt = bucket.list_grants()
   for name in lt:
       print name.permission, name.id, name.Grant, name.NameSpace, name.display_name, name.email_address, name.type, name.uri

if __name__ == "__main__":
   conn = boto.connect_s3()
   bucketname = "101-s3-aws"
   listgrants(bucketname)
