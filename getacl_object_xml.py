#!/usr/bin/python

"""
- Author : Nag m
- Hack   : Get the ACL of the object as xml
- Info   : Get the ACL of the object as xml
            * 101-s3-aws
"""

import boto

def acl(name):
   bucket = conn.get_bucket(name)
   key =  bucket.get_key("myfile1.txt")
   key_acl = key.get_acl()
   print key_acl.to_xml()


if __name__ == "__main__":
   conn = boto.connect_s3()
   bucketname = "101-s3-aws"
   acl(bucketname)
