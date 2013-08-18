#!/usr/bin/python

"""
- Author : Nag m
- Hack   : Set a canned ACL for object, canned_bucket_owner_read
- Info   : Set a canned ACL for object, canned_bucket_owner_full_control, useful when writing to different AWS Accounts
            * 101-s3-aws
"""

import boto

def canned(name):
   bucket = conn.get_bucket(name)
   key =  bucket.get_key("myfile1.txt")
   key.set_canned_acl('bucket-owner-read')


if __name__ == "__main__":
   conn = boto.connect_s3()
   bucketname = "101-s3-aws"
   canned(bucketname)

