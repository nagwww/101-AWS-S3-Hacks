#!/usr/bin/python

"""
- Author : Nag m
- Hack   : Set up CORS for an S3 bucket
- Info   : Set up CORS for an S3 bucket
            * 101-s3-aws
"""

import boto

def cors(name):
   bucket = conn.get_bucket(name)
   cors = boto.s3.cors.CORSConfiguration()
   cors.add_rule('GET','www.google.com',allowed_header="*")

if __name__ == "__main__":
   conn = boto.connect_s3()
   bucketname = "101-s3-aws"
   cors(bucketname)
