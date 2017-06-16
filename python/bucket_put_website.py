#!/usr/bin/python

"""
- Hack   : Set up a website for an S3 bucket
- AWS CLI: aws s3api put-bucket-website --bucket us-west-2.nag --website-configuration  file://./website.json
[ Copy the below policy to f.json ]
"""

import json
import boto3

p = {
    "IndexDocument": {
        "Suffix": "index.html"
    }
}

if __name__ == "__main__":
    client = boto3.client('s3')
    bucketname = "us-west-2.nag"
    print client.put_bucket_website(Bucket=bucketname, WebsiteConfiguration=p)
