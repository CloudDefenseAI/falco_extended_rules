#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import os

# Set the path to the file or directory you want to modify
path ="/home/f/syscall_analysis/creating_a_system_service_which_will"

# Set the desired ownership
owner = "falco4"

# Set the desired access permissions
permissions = "777" # for example, 755 or 644

# Change ownership
os.system("chown " + owner + " " + path)

# Change permissions
os.system("chmod " + permissions + " " + path)

