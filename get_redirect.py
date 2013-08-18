#!/usr/bin/python

"""
- Author : Nag m
- Hack   : Get the redirect for an S3 object
- Info   : Get the redirect for an S3 object
"""

import boto

def redirect():
   bucket = conn.get_bucket("101-s3-aws")
   obj = bucket.get_key("myfile1.txt")
   print obj.get_redirect()

if __name__ == "__main__":
   conn = boto.connect_s3()
   redirect()
