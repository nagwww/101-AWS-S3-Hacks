#!/usr/bin/python

"""
- Author : Nag m
- Hack   : Get the website configuration for this s3 bucket
- Info   : Get the website configuration for this s3 bucket
            * 101-s3-aws
"""

import boto

def website(name):
   bucket = conn.get_bucket(name)
   print bucket.get_website_configuration()

if __name__ == "__main__":
   conn = boto.connect_s3()
   bucketname = "101-s3-aws"
   website(bucketname)
