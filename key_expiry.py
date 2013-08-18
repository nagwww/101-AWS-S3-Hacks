#!/usr/bin/python

"""
- Author : Nag m
- Hack   : Get an expiry date of a key/object in S3
- Info   : Get an expiry date of a key/object in S3
  	   * myfile.txt
"""

import boto

def expiary():
   bucket = conn.get_bucket("101bucket")
   for key in bucket:
       print key.name, key.expiry_date

if __name__ == "__main__":
   conn = boto.connect_s3()
   expiary()
