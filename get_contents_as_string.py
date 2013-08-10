#!/usr/bin/python

"""
- Author : Nag m
- Hack   : Get the contents of the object as a string
- Info   : Get the contents of the object as a string
            * 101-s3-aws
"""

import boto

def copy(name):
   bucket = conn.get_bucket(name)
   key =  bucket.get_key("myfile1.txt")
   print key.get_contents_as_string()


if __name__ == "__main__":
   conn = boto.connect_s3()
   bucketname = "101-s3-aws"
   copy(bucketname)
