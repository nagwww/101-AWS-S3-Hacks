#!/usr/bin/python

"""
- Hack   : Create a bucket lifecycle policy
- AWS CLI: aws s3api put-bucket-lifecycle-configuration --bucket us-west-2.nag --lifecycle-configuration  file://./f.json [ Copy the below policy to f.json ]
"""

import json
import boto3

p = {
    "Rules": [
        {
            "Status": "Enabled",
            "Prefix": "",
            "ID": "Move old versions to Glacier",
            "Expiration": {
                "Days": 5
            }
        }
    ]
}

if __name__ == "__main__":
    client = boto3.client('s3')
    bucketname = "us-west-2.nag"
    print client.put_bucket_lifecycle_configuration(Bucket=bucketname, LifecycleConfiguration=p)
