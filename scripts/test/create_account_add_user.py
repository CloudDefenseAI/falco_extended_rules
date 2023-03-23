#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import subprocess

# Define the username and home directory
username = "falco5"
home_dir = "/home/falco5"

# Create the new user account
subprocess.run(["adduser", "--home", home_dir, "--shell", "/bin/bash", username])

# Set a password for the new user
subprocess.run(["passwd", username])

# Add the new user to a specific group 
subprocess.run(["sudo", "usermod", "-aG", "root", username])

