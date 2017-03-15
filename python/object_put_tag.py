#!/usr/bin/python

"""
- Author : Nag m
- Hack   : Tag an S3 object
- AWS CLI: aws s3api put-object-tagging  --bucket us-west-2.nag --key hello.txt --tagging 'TagSet=[{Key=name,Value=nag}]'
"""

import boto3

if __name__ == "__main__":
    client = boto3.client('s3')
    bucketname = "us-west-2.nag"
    print client.put_object_tagging(Bucket=bucketname, Key="hello.txt",
                                    Tagging={"TagSet": [{"Key": "Name", "Value": "Nag"}, ]})
