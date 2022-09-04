"""
A python program to perform basic object operations using AWS SDK for Python (Boto3) with Amazon Simple Storage Service
(Amazon S3) 
"""

import boto3 # AWS-SDK for python
import argparse # Parser for command-line options, arguments 

# create a client object
s3_client = boto3.client('s3')

# create a resource object
s3_resource = boto3.resource('s3')

# upload files to S3
def upload(namespace):
    s3_client.upload_file(
        namespace.file,
        namespace.bucket,
        namespace.file
    )
    response_message = 'File '+namespace.file+' uploaded on bucket '+namespace.bucket+' successfully'
    return response_message

# download files to S3
def download(namespace):
    s3_client.download_file(
        namespace.bucket,
        namespace.object,
        namespace.file
    )
    response_message = 'Object '+namespace.object+' downloaded from bucket '+namespace.bucket+' as '+namespace.file+' successfully'
    return response_message

# list all files in a S3 bucket
def list(namespace):
    objects = s3_client.list_objects(
        Bucket = namespace.bucket,
    )

    # if the bucket is empty
    if 'Contents' not in objects:
        print('Bucket',namespace.bucket,'is empty')
    # print all the names of the objects in the bucket
    else :
        for i in objects['Contents']:
            print(i['Key'])   

# delete an object in the bucket
def delete(namespace):
    s3_client.delete_objects(
        Bucket = namespace.bucket,
        Key = namespace.object
    )

# delete all objects in the bucket
def delete_all(namespace):
    s3_bucket = s3_resource.Bucket(namespace.bucket)
    
    # get all the object keys from the bucket and delete them
    s3_bucket.objects.all().delete()        
    response_message = 'Bucket '+namespace.bucket+' emptied'
    return response_message

# creating argument parser object
parser = argparse.ArgumentParser(description='Description: AWS S3 CLI')
subparsers = parser.add_subparsers(help='sub-command help')

# list
ls = subparsers.add_parser('list', help='List all objects in S3 Bucket')
ls.add_argument('--bucket', help='bucket name', required=True)
ls.set_defaults(func=list)

# upload
put = subparsers.add_parser('store', help='Upload a file to S3 Bucket')
put.add_argument('--bucket', help="bucket name", required=True)
put.add_argument('--file', help="file to be uploaded", required=True)
put.set_defaults(func=upload)

# download
get = subparsers.add_parser('get', help='Download an object from S3 Bucket')
get.add_argument('--bucket', help="bucket name", required=True)
get.add_argument('--object', help="key of the object", required=True)
get.add_argument('--file', help="file to be saved as", required=True)
get.set_defaults(func=download)

# delete
rm = subparsers.add_parser('remove', help="Delete an object from S3 Bucket")
rm.add_argument('--bucket', help="bucket name", required=True)
rm.add_argument('--object', help="key of the object", required=True)
rm.set_defaults(func=delete)

# delete all
Del = subparsers.add_parser('deleteAll', help="Delete all objects in S3 Bucket")
Del.add_argument('--bucket', help="bucket name", required=True)
Del.set_defaults(func=delete_all)

# parsing arguments to args
args = parser.parse_args()

try:
    response = args.func(args)
    if response: 
        print(response)
except Exception as Error:
    print("Error :", Error)

"""
To run the script,

# List all the files in the s3 bucket
python3 s3.py list --bucket=<bucket-name>

# Upload a file to the s3 bucket
python3 s3.py store --file=<file-location>  --bucket=<bucket-name>

# Download an object from the s3 bucket
python3 s3.py get --bucket=<bucket-name> --file=<file-location> --object=<object-key>

# Remove the specified object from the s3 bucket
python3 s3.py remove --bucket=<bucket-name> --object=<object-key>

# Delete all objects in the s3 bucket
python3 s3.py deleteAll --bucket=<bucket-name>

"""