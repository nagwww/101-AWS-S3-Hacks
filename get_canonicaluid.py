#!/usr/bin/python

"""
- Author : Nag m
- Hack   : Get the canonical user id of the S3 bucket
- Info   : Get the canonical user id of the S3 bucket
"""

import boto

def searchabucket():
   bucket = conn.lookup("eu-west-1.101-s3-aws")
   print bucket.get_location()

if __name__ == "__main__":
   conn = boto.connect_s3(host='s3-eu-west-1.amazonaws.com')
   searchabucket()
