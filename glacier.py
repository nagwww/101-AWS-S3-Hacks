#!/usr/bin/python

"""
- Author : Nag m
- Hack   : Move s3 objects to Glacier
- Info   : Move s3 objects to Glacier
            * 101-s3-aws
"""

import boto
from boto.s3.lifecycle import Lifecycle, Expiration, Rule


def glacier(name):
   bucket = conn.get_bucket(name)
   to_glacier = boto.s3.lifecycle.Transition(days=30, storage_class='GLACIER')
   rule = Rule('ruleid', 'logs/', 'Enabled', transition=to_glacier)
   lifecycle = Lifecycle()
   lifecycle.append(rule)
   bucket.configure_lifecycle(lifecycle)

if __name__ == "__main__":
   conn = boto.connect_s3()
   bucketname = "101bucket"
   glacier(bucketname)
