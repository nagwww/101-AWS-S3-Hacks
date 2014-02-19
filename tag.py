#!/usr/bin/python

"""
- Author : Nag m
- Hack   : Convert tags to key value pairs
- Info   : Convert tags to key value pairs
            * 101-s3-aws
"""

import boto
import xml.etree.ElementTree as ET

def tag(name):
   tag_k = []
   tag_v = []
   bucket = conn.get_bucket(name)
   tagset = bucket.get_tags()
   root = ET.fromstring(tagset.to_xml())
   for val in root.iter('Tag'):
     for child in val:
         if child.tag in "Key":
            tag_k.append(child.text)
         if child.tag in "Value":
            tag_v.append(child.text)
   s3tags = dict(zip([1,2,3,4], ['a', 'b', 'c', 'd']))
   print s3tags

if __name__ == "__main__":
   conn = boto.connect_s3()
   bucketname = "101-s3-aws"
   tag(bucketname)
