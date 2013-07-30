#!/usr/bin/python

"""
- Author : Nag m
- How to set the debugging
  * 101-s3-aws
"""

import boto

def searchabucket():
   bucket = conn.lookup("101-s3-aws")
   print bucket.name

if __name__ == "__main__":
   conn = boto.connect_s3(debug=3)
   searchabucket()
