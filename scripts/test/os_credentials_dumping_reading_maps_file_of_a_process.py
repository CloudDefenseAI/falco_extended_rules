#!/usr/bin/env python
# coding: utf-8

# In[ ]:


pid = 1767  # Replace with the desired process ID

maps_file_path = f"/proc/{pid}/maps"

with open(maps_file_path, "r") as f:
    maps_contents = f.read()

print(maps_contents)

