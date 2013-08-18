#!/usr/bin/python

"""
- Author : Nag m
- Hack   : Add a tag to S3 bucket
- Info   : Add a tag to S3 bucket
            * 101-s3-aws
"""

import boto

def tag(name):
   bucket = conn.get_bucket(name)
   tagset = boto.s3.tagging.TagSet()
   tagset.add_tag("name","nag")
   tag = boto.s3.tagging.Tags()
   tag.add_tag_set(tagset)
   bucket.set_tags(tag)

if __name__ == "__main__":
   conn = boto.connect_s3()
   bucketname = "101-s3-aws"
   tag(bucketname)
