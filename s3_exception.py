#!/usr/bin/python

"""
- Author : Nag m
- Hack   : How to add an exception
- Info   : Add lifecycle to S3 bucket
            * 101-s3-aws
"""

import boto

def lifecycle(name):
   try:
       bucket = conn.get_bucket(name)
   except Exception, ex:
       print ex

if __name__ == "__main__":
   conn = boto.connect_s3()
   bucketname = "101Bucket"
   lifecycle(bucketname)
