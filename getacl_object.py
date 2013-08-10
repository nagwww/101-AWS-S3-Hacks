#!/usr/bin/python

"""
- Author : Nag m
- Hack   : Get the ACL of the object
- Info   : Get the ACL of the object
            * 101-s3-aws
"""

import boto

def copy(name):
   bucket = conn.get_bucket(name)
   key =  bucket.get_key("myfile1.txt")
   key_acl = key.get_acl()
   print key_acl
   print key_acl.parent
   for grant in key_acl.acl.grants:
      print grant.permission


if __name__ == "__main__":
   conn = boto.connect_s3()
   bucketname = "101-s3-aws"
   copy(bucketname)
