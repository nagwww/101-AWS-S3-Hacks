#!/usr/bin/python

"""
- Author : Nag m
- Hack   : Get the canonical user id of the S3 bucket
- Info   : Get the canonical user id of the S3 bucket
"""

import boto

def get_canonicaluid():
   print conn.get_canonical_user_id()

if __name__ == "__main__":
   conn = boto.connect_s3()
   get_canonicaluid()
