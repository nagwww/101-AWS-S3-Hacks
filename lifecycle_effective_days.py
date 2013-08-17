#!/usr/bin/python

"""
- Author : Nag m
- Hack   : Add lifecycle to S3 bucket, set the effective days
- Info   : Add lifecycle to S3 bucket, set the effective days
            * 101-s3-aws
"""

import boto
from boto.s3.lifecycle import Lifecycle, Expiration

def lifecycle(name):
   bucket = conn.get_bucket(name)
   lifecycle_config = boto.s3.lifecycle.Lifecycle()
   lifecycle_config.add_rule("lc1","/", "Enabled",expiration=Expiration(days=30))
   bucket.configure_lifecycle(lifecycle_config)

if __name__ == "__main__":
   conn = boto.connect_s3()
   bucketname = "101bucket"
   lifecycle(bucketname)
