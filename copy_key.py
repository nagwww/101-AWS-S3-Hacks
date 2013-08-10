#!/usr/bin/python

"""
- Author : Nag m
- Hack   : Copy the current key to a different Bucket
- Info   : Copy the current key to a different bucket
            * 101-s3-aws
"""

import boto

def copy(name):
   bucket = conn.get_bucket(name)
   key = bucket.get_key("myfile1.txt")

   dst_bucket = conn.get_bucket("101bucket")
   print key.copy(dst_bucket,"test.txt")

if __name__ == "__main__":
   conn = boto.connect_s3()
   bucketname = "101-s3-aws"
   copy(bucketname)
