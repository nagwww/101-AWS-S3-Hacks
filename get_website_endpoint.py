#!/usr/bin/python

"""
- Author : Nag m
- Hack   : Get the website_endpoint of a s3 bucket
- Info   : Get the  website_endpoint of a s3 bucket
            * 101-s3-aws
"""

import boto
import json

def getendpoint(name):
   bucket = conn.get_bucket(name)
   print  bucket.get_website_endpoint()

if __name__ == "__main__":
   conn = boto.connect_s3()
   bucketname = "101-s3-aws"
   getendpoint(bucketname)
