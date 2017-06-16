#!/usr/bin/python

"""
- Hack   : Set up bucket replication
- AWS CLI: aws s3api put-bucket-replication --bucket us-west-2.nag --replication-configuration  file://./replication.json [ Copy the below policy to f.json ]
"""

import json
import boto3

p = {

    "Rules": [
        {
            "Status": "Enabled",
            "Prefix": "",
            "Destination": {
                "Bucket": "arn:aws:s3:::us-east-1.nag",
                "StorageClass": "STANDARD"
            },
            "ID": "us-west-2.nag1"
        }
    ],
    "Role": "arn:aws:iam::220580744359:role/service-role/replication_role_for_us-west-2.nag_to_us-east-1.nag"
}

if __name__ == "__main__":
    client = boto3.client('s3')
    bucketname = "us-west-2.nag"
    print client.put_bucket_replication(Bucket=bucketname, ReplicationConfiguration=p)
