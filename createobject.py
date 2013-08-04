#!/usr/bin/python

"""
- Author : Nag m
- Hack   : Create a new object in S3
- Info   : Create a object named
 	   - myfile.txt
"""

import boto

def createaobject():
   bucket = conn.get_bucket("101-s3-aws")
   obj = bucket.new_key("myfile.txt")
   obj.set_contents_from_string("This is my first object created in S3") 

if __name__ == "__main__":
   conn = boto.connect_s3()
   createaobject()
