#!/usr/bin/python

"""
- Author : Nag m
- Get all the S3 regions
"""

import boto
from boto.s3.connection import Location

def getregions():
    for region in dir(Location):
        if region[0].isupper():
           print region

if __name__ == "__main__":
    getregions()
