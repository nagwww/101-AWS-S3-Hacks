#!/usr/bin/python

"""
- Author : Nag m
- Hack   : Get the get_xml_acl of an S3 object
- Info   : Get the get_xml_acl of an s3 object
            * 101-s3-aws
"""

import boto

def copy(name):
   bucket = conn.get_bucket(name)
   key =  bucket.get_key("myfile1.txt")
   print key.get_xml_acl()


if __name__ == "__main__":
   conn = boto.connect_s3()
   bucketname = "101-s3-aws"
   copy(bucketname)
