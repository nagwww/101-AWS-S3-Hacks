#!/usr/bin/python

"""
- Author : Nag m
- Hack   : Get status of the restore of an object from glacier
- Info   : Get status of the restore of an object from glacier
  	   * myfile.txt
"""

import boto

def restore():
   bucket = conn.get_bucket("101-s3-aws")
   obj = bucket.get_key("myfile1.txt")
   print obj.ongoing_restore


if __name__ == "__main__":
   conn = boto.connect_s3()
   restore()
