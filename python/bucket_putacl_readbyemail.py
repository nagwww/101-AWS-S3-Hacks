#!/usr/bin/python

"""
- Author : Nag m
- Hack   : Grant read access to a bucket by email
- AWS CLI: aws s3api put-bucket-acl --bucket us-west-2.nag --grant-read emailaddress=test@gmail.com

"""

import json
import boto3

acp = {
    "Grants": [
        {
            "Grantee": {
                "Type": "AmazonCustomerByEmail",
                "EmailAddress": "test@gmail.com"
            },
            "Permission" : "READ"
        }

    ],
    "Owner" : {
        "DisplayName": "nagm",
        "ID": "ba54237358a1eaafd46b0xxxxxx3e9e25429b401cc"

      }
}

if __name__ == "__main__":
    client = boto3.client('s3')
    bucketname = "us-west-2.nag"
    print client.put_bucket_acl(Bucket=bucketname, AccessControlPolicy=acp)
