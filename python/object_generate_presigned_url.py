#!/usr/bin/python

"""
- Hack   : Generate a presigned url
- AWS CLI: There is no CLI
"""

import boto3

if __name__ == "__main__":
    client = boto3.client('s3', region_name="us-west-2")
    bucketname = "us-west-2.nag"
    post_url = client.generate_presigned_url('get_object', {'Bucket': bucketname , 'Key':'hello1.txt' }, ExpiresIn=3600)
    print "URL to test : ", post_url
