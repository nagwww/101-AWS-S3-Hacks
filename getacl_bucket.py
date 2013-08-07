#!/usr/bin/python

"""
- Author : Nag m
- Hack   : Get the ACL of the S3 bucket
- Info   : Get the ACL of the s3 bucket
            * 101-s3-aws
"""

import boto

def getacl(name):
   bucket = conn.get_bucket(name)
   bucket_acl =  bucket.get_acl()
   print bucket_acl
   for grant in bucket_acl.acl.grants:
      print grant.permission

if __name__ == "__main__":
   conn = boto.connect_s3()
   bucketname = "101-s3-aws"
   getacl(bucketname)
