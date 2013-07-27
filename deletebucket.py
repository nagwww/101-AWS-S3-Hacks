#!/usr/bin/python

"""
- Author : Nag m
- Delete a bucket named
  * 101-s3-aws
"""

import boto

def deletebucket(name):
   bucket = conn.delete_bucket(name)

if __name__ == "__main__":
   conn = boto.connect_s3()
   bucketname = "101-s3-aws"
   deletebucket(bucketname)
