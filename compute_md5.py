#!/usr/bin/python

"""
- Author : Nag m
- Hack   : Compute MD5 for an S3 object
- Info   : Compute MD5 for an S3 object
            * 101-s3-aws
"""

import boto

def md5(name):
   bucket = conn.get_bucket(name)
   key = bucket.get_key("myfile1.txt")
   print eval(key.etag)

if __name__ == "__main__":
   conn = boto.connect_s3()
   bucketname = "101-s3-aws"
   md5(bucketname)
