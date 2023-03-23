#!/usr/bin/env python
# coding: utf-8

# In[8]:


import subprocess

# Execute the systemctl command and capture the output
output = subprocess.check_output(['systemctl', 'list-unit-files', '--type=service'])

# Split the output into lines
lines = output.decode().split('\n')
print(lines)



# In[ ]:




