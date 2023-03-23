#!/usr/bin/env python
# coding: utf-8

# In[3]:


# Open and read the Bash history file
user="ashutoshreddy"
file=f"/home/{user}/.bash_history"
with open(".bash_history", "r") as f:
    lines = f.readlines()



for line in lines:
    print(line.strip())


# In[ ]:




