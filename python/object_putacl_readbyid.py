#!/usr/bin/python

"""
- Author : Nag m
- Hack   : Grant read access to an object by email
- AWS CLI: aws s3api put-object-acl --bucket us-west-2.nag --key hello.txt --grant-read id=xxxxxxxx

"""

import json
import boto3

acp = {
    "Grants": [
        {
            "Grantee": {
                "Type": "CanonicalUser",
                "ID": "237358a1eaafd46b06257a8e7a8023f71e243b86bfaef3e9e25429b401cc"
            },
            "Permission": "READ"
        }

    ],
    "Owner": {
        "DisplayName": "nagm",
        "ID": "31eaafd46b06257a8e7a8023f71e243b86bfaef3e9e25429b401cc"

    }
}

if __name__ == "__main__":
    client = boto3.client('s3')
    bucketname = "us-west-2.nag"
    print client.put_object_acl(Bucket=bucketname, AccessControlPolicy=acp, Key="hello.txt")
