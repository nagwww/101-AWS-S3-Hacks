#!/usr/bin/python

"""
- Author : Nag m
- Hack   : Restore an object from glacier
- Info   : Restore an object from glacier
  	   * myfile.txt
"""

import boto

def restore():
   bucket = conn.get_bucket("101-s3-aws")
   obj = bucket.get_key("myfile1.txt")
   obj.restore(days=5)


if __name__ == "__main__":
   conn = boto.connect_s3()
   restore()
