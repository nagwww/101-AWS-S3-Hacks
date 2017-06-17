#!/usr/bin/python

"""
- Hack   : Generate a presigned url for post
- AWS CLI: N/A
"""

import json
import boto3

if __name__ == "__main__":
    client = boto3.client('s3', region_name="us-west-2")
    bucketname = "us-west-2.nag"
    post_url = client.generate_presigned_post(Bucket=bucketname, Key="hello1.txt", ExpiresIn=3600,
                                         Fields={"acl": "public-read", "Content-Type": "html/txt"},
                                         Conditions=[
                                             {"acl": "public-read"},
                                             {"Content-Type": "html/txt"}
                                         ],
                                         )
    print "URL to test : ", 'https://{}.s3.amazonaws.com/{}'.format(bucketname,"hello1.txt"), post_url
