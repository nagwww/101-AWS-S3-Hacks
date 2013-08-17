#!/usr/bin/python

"""
- Author : Nag m
- Hack   : Delete all files in a folder
- Info   : Delete all files in a folder
            * 101-s3-aws
"""

import boto

def listobj(name):
   bucket = conn.get_bucket(name)
   bucketListResultSet = bucket.list(prefix="folder")
   bucket.delete_keys([key.name for key in bucketListResultSet])

if __name__ == "__main__":
   conn = boto.connect_s3()
   bucketname = "101-s3-aws"
   listobj(bucketname)
