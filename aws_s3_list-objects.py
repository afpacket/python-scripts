#!/usr/bin/env python3

import boto3
from argparse import ArgumentParser
from botocore.exceptions import ClientError

def main():
   parser = ArgumentParser()
   parser.add_argument("bucket_name", type=str,
                       help="S3 bucket name")

   args = parser.parse_args()
   client = boto3.client('s3')
   s3_bucket_name = args.bucket_name

   s3_list_objects(client, s3_bucket_name)

def s3_list_objects(client, s3_bucket_name):
    """List objects in S3 Bucket"""
    try:
        for s3_object in client.list_objects_v2(Bucket=s3_bucket_name)['Contents']:
            print(s3_object['Key'])
    except ClientError as error:
           print(f"error: { error }")

if __name__ == "__main__":
   main()
