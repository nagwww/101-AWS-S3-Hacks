#!/usr/bin/python

"""
- Author : Nag m
- Hack   : Add ACL to the bucket. Grant Read privilages to the bucket using email address of another AWS Account
- Info   : Add ACL to the bucket. Grant READ privilages to the bucket using email address of the AWS Account
            * 101-s3-aws
"""

import boto

def addacl(name):
   bucket = conn.get_bucket(name)
   bucket.add_email_grant("READ","nagwww@gmail.com")
   print "Added ACL to the Bucket named ", bucket.name, " "

if __name__ == "__main__":
   conn = boto.connect_s3()
   bucketname = "101-s3-aws"
   addacl(bucketname)
