#!/usr/bin/python

"""
- Author : Nag m
- Hack   : Set metadata for a new s3 object on creation
- Info   : Set metadata for a new s3 object on creation
 	   * myfile.txt
	  set_contents_from_filename vs send_file. set_contents_from_filename uses send_file
"""

import boto

def uploadfile():
   bucket = conn.get_bucket("101-s3-aws")
   obj = bucket.new_key("myfile1.txt")
   obj.set_metadata("time", "pst")
   obj.set_contents_from_filename("myfile.txt") 

if __name__ == "__main__":
   conn = boto.connect_s3()
   uploadfile()
