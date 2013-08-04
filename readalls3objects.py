#!/usr/bin/python

"""
- Author : Nag m
- Hack   : List all the objects in a S3 bucket
- Info   : Lists all objects in a bucket
	   The name of the bucket is
   	   * 101-s3-aws
"""

import boto

def getallobjects(name):
   buck = conn.get_bucket(name)
   for key in buck:
       print key.name

if __name__ == "__main__":
   conn = boto.connect_s3()
   bucketname = "101-s3-aws"
   getallobjects(bucketname)
