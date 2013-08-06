#!/usr/bin/python

"""
- Author : Nag m
- Hack   : Enable Versioning 
- Info   : Enable Versioming
            * 101-s3-aws
"""

import boto

def addacl(name):
   bucket = conn.get_bucket(name)
   print bucket.configure_versioning(True)

if __name__ == "__main__":
   conn = boto.connect_s3()
   bucketname = "101-s3-aws"
   addacl(bucketname)
