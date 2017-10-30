#!/usr/bin/python

"""
- Author : Nag m
- Hack   : Delete the inventory configurations for an S3 bucket.
- AWS CLI: aws s3api delete-bucket-inventory-configuration --bucket us-west-2.nag --Id nagbucket
"""

import boto3

if __name__ == "__main__":
    client = boto3.client('s3')
    bucketname = "us-west-2.nag"
    analytics_config = client.delete_bucket_inventory_configuration(Bucket=bucketname, Id="nagbucket")
#    print analytics_config["InventoryConfiguration"]
