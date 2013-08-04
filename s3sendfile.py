#!/usr/bin/python

"""
- Author : Nag m
- Hack   : Upload a file to s3 bucket using the method send_file
- Info   : Upload a file named
  	   - myfile.txt
	   set_contents_from_filename vs send_file. set_contents_from_filename uses send_file
	   Getting a HTTP 400 error
"""

import boto

def uploadfile():
   bucket = conn.get_bucket("101-s3-aws")
   obj = bucket.new_key("myfile2.txt")
   fp = open("myfile.txt", "r")
   obj.send_file(fp) 

if __name__ == "__main__":
   conn = boto.connect_s3()
   uploadfile()
