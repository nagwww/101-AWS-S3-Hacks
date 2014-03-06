#!/usr/bin/python2.7

"""
- Author : Nag m
- Hack   : Use STS to connect to a different AWS Account and delete objects
- Info   : Use STS to connect to a different AWS Account and delete objects
            * 101-s3-aws
"""

import boto
from boto.s3.connection import OrdinaryCallingFormat

def del(name):
   bucket = s3conn.get_bucket(name)
   for obj in bucket.list():
       print " Deleting ... ", obj.name, obj.delete()

if __name__ == "__main__":
   account = "1222222222222"
   role = 'arn:aws:iam::' + account + ':role/Role1'
   stsconn = boto.connect_sts()
   c = stsconn.assume_role(role, 'rolename')
   s3conn = boto.connect_s3(c.credentials.access_key, c.credentials.secret_key, security_token=c.credentials.session_token,calling_format=OrdinaryCallingFormat(),host='s3-us-west-2.amazonaws.com')
   bucketname = "us-west-2.test.test"
   del(bucketname)
