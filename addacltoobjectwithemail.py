#!/usr/bin/python

"""
- Author : Nag m
- Hack   : Add ACL to an object. Grant Read privilages to the bucket using email address
- Info   : Add ACL to an object. Grant READ privilages to the bucket using email address of the AWS Account
            * 101-s3-aws
"""

import boto

def addacl(name):
   bucket = conn.get_bucket(name)
   key = bucket.get_key("myfile1.txt")
   key.add_email_grant("READ","nagwww@gmail.com")
   print "Added ACL to the Object named ", key.name, " "

if __name__ == "__main__":
   conn = boto.connect_s3()
   bucketname = "101-s3-aws"
   addacl(bucketname)
