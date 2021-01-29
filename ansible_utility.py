import boto3
import os
import logging
import botocore

bucket_name = 'zolabs-ssm-association'
s3_folder = '/roles'
object_name = 'rhel-apache.yml'
file_name = object_name

# Func to downloand Ansible roles from S3
def s3_download_folder(bucket_name, s3_folder, local_dir=None):
    
    s3 = boto3.resource('s3')
    bucket = s3.Bucket(bucket_name)
    test = bucket.objects.filter(Prefix="roles")
    for obj in bucket.objects.filter(Prefix="roles"):
        target = obj.key if local_dir is None \
            else os.path.join(local_dir, os.path.relpath(obj.key, s3_folder))
        if not os.path.exists(os.path.dirname(target)):
            os.makedirs(os.path.dirname(target))
        if obj.key[-1] == '/':
            continue
        bucket.download_file(obj.key, target)

# Call s3_downnload
s3_download_folder(bucket_name, s3_folder)


# func to download the Ansible's main root playbook
def s3_download_file(bucket_name, object_name, file_name):

    s3 = boto3.client('s3')
    s3.download_file(bucket_name, object_name, file_name)

# call s3_download)file
s3_download_file(bucket_name, object_name, file_name)



