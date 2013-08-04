#!/usr/bin/python

"""
- Author : Nag m
- Hack   : Create a folder in a S3 bucket
- Info   : Create a folder named
  	   - Folder
	   - Placing a "/" at the end of the object name creates a folder
"""

import boto

def createafolder():
   bucket = conn.get_bucket("101-s3-aws")
   obj = bucket.new_key("folder/")

if __name__ == "__main__":
   conn = boto.connect_s3()
   createafolder()
