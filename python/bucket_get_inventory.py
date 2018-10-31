#!/usr/bin/python

"""
- Author : Nag m
- Hack   : Get the inventory configurations for an S3 bucket.
- AWS CLI: aws s3api get-bucket-inventory-configuration --bucket us-west-2.nag
"""

import boto3

if __name__ == "__main__":
    client = boto3.client('s3')
    bucketname = "us-west-2.nag"
    analytics_config = client.get_bucket_inventory_configuration(Bucket=bucketname, Id="nagbucket")
    print analytics_config["InventoryConfiguration"]
