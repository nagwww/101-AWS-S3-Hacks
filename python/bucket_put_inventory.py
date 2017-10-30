#!/usr/bin/python

"""
- Author : Nag m
- Hack   : Create inventory configurations for an S3 bucket.
- AWS CLI: aws s3api get-bucket-inventory-configuration --bucket us-west-2.nag
"""

config = {
        "Schedule": {
            "Frequency": "Daily"
        }, 
        "IsEnabled": True, 
        "Destination": {
            "S3BucketDestination": {
                "Bucket": "arn:aws:s3:::us-west-2.nag", 
                "Format": "CSV"
            }
        }, 
        "OptionalFields": [
            "Size", 
            "LastModifiedDate", 
            "StorageClass"
        ], 
        "IncludedObjectVersions": "Current", 
        "Id": "nag"
    }


import boto3

if __name__ == "__main__":
    client = boto3.client('s3')
    bucketname = "us-west-2.nag"
    inventory_config = client.put_bucket_inventory_configuration(Bucket=bucketname, InventoryConfiguration=config, Id="nag")
    print inventory_config
