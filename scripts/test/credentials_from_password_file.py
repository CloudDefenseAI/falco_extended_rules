#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import os

username = 'dummy'
home_dir = '/home/du'
user_id = '1001'
group_id = '1001'
comment = 'New User'
shell = '/bin/bash'

with open('/etc/passwd', 'a') as passwd_file:
    passwd_file.write(f"{username}:x:{user_id}:{group_id}:{comment}:{home_dir}:{shell}\n")

os.system('passwd newuser')

