#!/usr/bin/python

"""
- Author : Nag m
- Delete a object named
  * myfile.txt
"""

import boto

def deleteaobject():
   bucket = conn.get_bucket("101-s3-aws")
   obj = bucket.delete_key("myfile.txt")

if __name__ == "__main__":
   conn = boto.connect_s3()
   deleteaobject()
