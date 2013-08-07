#!/usr/bin/python

"""
- Author : Nag m
- Hack   : Set the meta data for an object
- Info   : Set the meta data for an object
            - Metadata can only be set at the time the object is written to S3 or when it is copied.
            - https://github.com/boto/boto/issues/1007
            * 101-s3-aws
"""

import boto

metadata = {'name':'Mr. Nag'}

def listobj(name):
   bucket = conn.get_bucket(name)
   for obj in bucket:
       obj.copy(bucket.name, obj.name, metadata, preserve_acl=True)

if __name__ == "__main__":
   conn = boto.connect_s3()
   bucketname = "101-s3-aws"
   listobj(bucketname)
