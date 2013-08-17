#!/usr/bin/python

"""
- Author : Nag m
- Hack   : Generate a URL for the S3 object with expiration of 5 min
- Info   : Generate a URL for the S3 object with expiration of 5 min
            * 101-s3-aws
"""

import boto

def copy(name):
   bucket = conn.get_bucket(name)
   key =  bucket.get_key("myfile1.txt")
   print key.generate_url(300)


if __name__ == "__main__":
   conn = boto.connect_s3()
   bucketname = "101-s3-aws"
   copy(bucketname)
