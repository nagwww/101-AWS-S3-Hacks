#!/usr/bin/python

"""
- Author : Nag m
- Hack   : Set set_request_payment for a bucket
- Info   : Set set_request_payment for a bucket
            * 101-s3-aws
"""

import boto

def payment(name):
   bucket = conn.get_bucket(name)
   print bucket.set_request_payment

if __name__ == "__main__":
   conn = boto.connect_s3()
   bucketname = "101-s3-aws"
   payment(bucketname)
