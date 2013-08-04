#!/usr/bin/python

"""
- Author : Nag m
- Hack   : Download a file using the method get_file
- Info   : Download a file named using the method get_file
  	   * myfile.txt
"""

import boto

def downloadfile():
   bucket = conn.get_bucket("101-s3-aws")
   obj = bucket.get_key("myfile1.txt")
   fp = open ("myfile1.txt", "w")
   obj.get_file(fp) 

if __name__ == "__main__":
   conn = boto.connect_s3()
   downloadfile()
