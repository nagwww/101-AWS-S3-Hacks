#!/usr/bin/python

"""
- Author : Nag m
- Upload a file named
  * myfile.txt
"""

import boto

def downloadfile():
   bucket = conn.get_bucket("101-s3-aws")
   obj = bucket.get_key("myfile1.txt")
   obj.get_contents_to_filename("myfile1.txt") 

if __name__ == "__main__":
   conn = boto.connect_s3()
   downloadfile()
