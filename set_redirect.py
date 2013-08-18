#!/usr/bin/python

"""
- Author : Nag m
- Hack   : Set a redirect for an S3 object
- Info   : Set a redirect for an S3 object
"""

import boto

def redirect():
   bucket = conn.get_bucket("101-s3-aws")
   obj = bucket.get_key("myfile1.txt")
   obj.set_redirect("http://www.google.com")

if __name__ == "__main__":
   conn = boto.connect_s3()
   redirect()
