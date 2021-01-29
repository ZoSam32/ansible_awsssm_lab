import boto3
import os
import sys
import getopt
import logging
import botocore
import ansible_runner

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

# func to download the Ansible's main root playbook
def s3_download_file(bucket_name, object_name, file_name):

    s3 = boto3.client('s3')
    s3.download_file(bucket_name, object_name, file_name)

# function to run Ansible via ansible-runner wrapper
def ansible_runner_call(data_dir, playbook):
    r = ansible_runner.run(private_data_dir=data_dir, playbook=playbook)
    print("{}: {}".format(r.status, r.rc))
    # successfull: 0 
    for each_host_event in r.events:
        print("Final Status:")
        print(r.status)

if __name__ == "__main__":
    args= sys.argv[1:]

    bucket_name = ''
    s3_folder = ''
    object_name = ''
    
    try:
        opts, args = getopt.getopt(args,"b:f:r:")
    except getopt.GetoptError:
        print("send with vars dummy")
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-b':
            bucket_name = arg
        elif opt == '-f':
            s3_folder = arg
        elif opt == '-r':
            object_name = arg
    
    # object_name for local file name
    file_name = object_name

    # Call s3_downnload
    print(bucket_name)
    s3_download_folder(bucket_name, s3_folder)

    # call s3_download)file
    s3_download_file(bucket_name, object_name, file_name)

    # call Ansible-Runner
    data_dir = 'ansible-runner'
    playbook = object_name
    ansible_runner_call(data_dir, playbook)


