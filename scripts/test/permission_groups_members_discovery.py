#!/usr/bin/env python
# coding: utf-8

# In[2]:


import os

# Get list of groups
groups = {}
with open('/etc/group', 'r') as f:
    for line in f:
        group_info = line.strip().split(':')
        group_name = group_info[0]
        group_members = group_info[3].split(',')
        groups[group_name] = group_members

# Print list of groups and their members
print("Groups:\n")
for group, members in groups.items():
    print(f"  {group}: {', '.join(members)}\n")

# Get file permissions
files = ['/etc/group', '/etc/passwd', '/etc/shadow', '/etc/sudoers']
print("\nFile permissions:")
for file in files:
    try:
        mode = os.stat(file).st_mode
        print(f"  {file}: {oct(mode)[-3:]}\n")
    except FileNotFoundError:
        print(f"  {file} not found\n")


# In[ ]:




