#!/usr/bin/python

"""
- Author : Nag m
- Hack   : Set a canned ACL, private
- Info   : Set a canned ACL. private
            * 101-s3-aws
"""

import boto

def canned(name):
   bucket = conn.get_bucket(name)
   bucket.set_acl('private')

if __name__ == "__main__":
   conn = boto.connect_s3()
   bucketname = "101-s3-aws"
   canned(bucketname)
