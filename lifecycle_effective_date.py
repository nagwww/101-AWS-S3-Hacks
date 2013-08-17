#!/usr/bin/python

"""
- Author : Nag m
- Hack   : Add lifecycle to S3 bucket, set the effective date. Don't specify the time or specify GMT midnight
- Info   : Add lifecycle to S3 bucket, set the effective date
            * 101-s3-aws
"""

import boto
from boto.s3.lifecycle import Lifecycle, Expiration
import dateutil.parser as parser

def lifecycle(name):
   text = 'Thu, 16 Dec 2013'
   date = (parser.parse(text))
   d = date.isoformat()
   bucket = conn.get_bucket(name)
   lifecycle_config = boto.s3.lifecycle.Lifecycle()
   lifecycle_config.add_rule("lc1","/", "Enabled",expiration=Expiration(date=d))
   bucket.configure_lifecycle(lifecycle_config)

if __name__ == "__main__":
   conn = boto.connect_s3()
   bucketname = "101bucket"
   lifecycle(bucketname)
