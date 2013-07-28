#!/usr/bin/python

"""
- Author : Nag m
- Upload a file named
  * myfile.txt
"""

import boto

def uploadfile():
   bucket = conn.get_bucket("101-s3-aws")
   obj = bucket.new_key("myfile1.txt")
   obj.set_contents_from_filename("myfile.txt") 

if __name__ == "__main__":
   conn = boto.connect_s3()
   uploadfile()
