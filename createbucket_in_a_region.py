#!/usr/bin/python

"""
- Author : Nag m
- Hack   : Create a S3 bucket in a different region EU
- Info   : Create a bucket named 
	   - 101-s3-aws
 	   - Region eu-west-1
"""

import boto
from boto.s3.connection import Location

def createabucket(name):
   bucket = conn.create_bucket(name,location=Location.EU)
   print "Bucket named ", bucket.name, " created"

if __name__ == "__main__":
   conn = boto.connect_s3()
   bucketname = "eu-west-1.101-s3-aws"
   createabucket(bucketname)
