#!/usr/bin/python

"""
- Author : Nag m
- Hack   : Set a canned ACL for object, authenticated-read
- Info   : Set a canned ACL for object. authenticated-read
            * 101-s3-aws
"""

import boto

def canned(name):
   bucket = conn.get_bucket(name)
   key =  bucket.get_key("myfile1.txt")
   key.set_canned_acl('authenticated-read')


if __name__ == "__main__":
   conn = boto.connect_s3()
   bucketname = "101-s3-aws"
   canned(bucketname)

