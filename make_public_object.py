#!/usr/bin/python

"""
- Author : Nag m
- Hack   : Make an object public
- Info   : Make an object public
            * 101-s3-aws
"""

import boto

def copy(name):
   bucket = conn.get_bucket(name)
   key =  bucket.get_key("myfile1.txt")
   print key.make_public()


if __name__ == "__main__":
   conn = boto.connect_s3()
   bucketname = "101-s3-aws"
   copy(bucketname)
