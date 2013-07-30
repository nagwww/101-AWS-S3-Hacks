#!/usr/bin/python

"""
- Author : Nag m
- Make http connection to the S3 endpoint
- To confirm it is making a http connection run tcpdump you should see something thing like s3-1-w.amazonaws.com.http
- If it is a https then you should see something like s3-1-w.amazonaws.com.https
  * Bucket Name : 101-s3-aws
"""

import boto

def searchabucket():
   bucket = conn.lookup("101-s3-aws")
   print bucket.name

if __name__ == "__main__":
   conn = boto.connect_s3(debug=6,is_secure=False)
   searchabucket()
