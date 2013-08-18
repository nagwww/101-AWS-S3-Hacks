#!/usr/bin/python

"""
- Author : Nag m
- Hack   : Convert an existing key in an S3 bucket that uses the STANDARD  to RRS
- Info   : Convert an existing key in an S3 bucket that uses the STANDARD  to RRS
"""

import boto

def redundancy():
   bucket = conn.get_bucket("101-s3-aws")
   obj = bucket.get_key("myfile1.txt")
   print obj.change_storage_class('REDUCED_REDUNDANCY')

if __name__ == "__main__":
   conn = boto.connect_s3()
   redundancy()
