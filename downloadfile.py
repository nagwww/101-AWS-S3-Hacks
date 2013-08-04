#!/usr/bin/python

"""
- Author : Nag m
- Hack   : Download a S3 file or a S3 object
- Info   : Download a file named
  	   - myfile.txt
	   Using the method get_contents_to_filename.
	   The method get_contents_to_filename uses the method get_file internally
"""

import boto

def downloadfile():
   bucket = conn.get_bucket("101-s3-aws")
   obj = bucket.get_key("myfile1.txt")
   obj.get_contents_to_filename("myfile1.txt") 

if __name__ == "__main__":
   conn = boto.connect_s3()
   downloadfile()
