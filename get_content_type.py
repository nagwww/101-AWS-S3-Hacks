#!/usr/bin/python

"""
- Author : Nag m
- Hack   : Get the content type of object. Note only works with get_key 
- Info   : Get the content type of object. Note only works with get_key
           https://groups.google.com/forum/#!msg/boto-users/KIkux87DJyE/pOtRMTzGG5EJ
            * 101-s3-aws
"""

import boto

def listobj(name):
   bucket = conn.get_bucket(name)
   lt =  bucket.list()
   for obj in lt:
       print obj.content_type

   for key in lt:
        k = bucket.get_key(key.name)
        print k.name , k.content_type 

if __name__ == "__main__":
   conn = boto.connect_s3()
   bucketname = "101-s3-aws"
   listobj(bucketname)
