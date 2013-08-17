#!/usr/bin/python

"""
- Author : Nag m
- Hack   : Add lifecycle to S3 bucket
- Info   : Add lifecycle to S3 bucket
            * 101-s3-aws
"""

import boto

def lifecycle(name):
   bucket = conn.get_bucket(name)
   lifecycle_config = boto.s3.lifecycle.Lifecycle()
   lifecycle_config.add_rule("lc1","/", "Enabled",5)
   bucket.configure_lifecycle(lifecycle_config)

if __name__ == "__main__":
   conn = boto.connect_s3()
   bucketname = "101bucket"
   lifecycle(bucketname)
