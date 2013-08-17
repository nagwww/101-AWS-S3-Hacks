#!/usr/bin/python

"""
- Author : Nag m
- Hack   : Configure this bucket to act as a website
- Info   : Configure this bucket to act as a website
            * 101-s3-aws
"""

import boto

def lifecycle(name):
   bucket = conn.get_bucket(name)
   bucket.configure_website("index.html","error.html")

if __name__ == "__main__":
   conn = boto.connect_s3()
   bucketname = "101-s3-aws"
   lifecycle(bucketname)
