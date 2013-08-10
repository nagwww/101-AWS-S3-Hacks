#!/usr/bin/python

"""
- Author : Nag m
- Hack   : Set a private canned ACL for an object 
- Info   : Set a private canned ACL for an object
            * 101-s3-aws
"""

import boto

def copy(name):
   bucket = conn.get_bucket(name)
   key =  bucket.get_key("myfile1.txt")
   key.set_canned_acl('private')


if __name__ == "__main__":
   conn = boto.connect_s3()
   bucketname = "101-s3-aws"
   copy(bucketname)
