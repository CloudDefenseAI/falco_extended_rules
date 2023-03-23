#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import os
import shutil
import subprocess

# Function to create a tar archive
def create_tar_archive(directory_path, archive_name):
    archive_path = archive_name + '.tar.gz'
    subprocess.call(['tar', '-czf', archive_path, directory_path])
    return archive_path

# Function to create a zip archive
def create_zip_archive(directory_path, archive_name):
    archive_path = archive_name + '.zip'
    shutil.make_archive(archive_name, 'zip', directory_path)
    return archive_path

# Function to compress a file using gzip
def gzip_file(file_path):
    subprocess.call(['gzip', file_path])

# Function to compress a file using bzip2
def bzip2_file(file_path):
    subprocess.call(['bzip2', file_path])

# Example usage
if __name__ == '__main__':
    # Create a tar archive of the "data" directory
    create_tar_archive('/home/f/syscall_analysis', 'data_archive_tar')

    # Create a zip archive of the "data" directory
    create_zip_archive('/home/f/syscall_analysis', 'data_archive_zip')

    # Compress a file using gzip
    gzip_file('/home/f/syscall_analysis/cd')

    # Compress a file using bzip2
    bzip2_file('/home/f/syscall_analysis/ef')

