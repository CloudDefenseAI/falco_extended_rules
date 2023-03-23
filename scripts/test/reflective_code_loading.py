#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import os

# example directory to list
directory = "/home/f"

# using execve() system call
pid = os.fork()
if pid == 0:
    os.execve("/bin/ls", ["/bin/ls", directory], os.environ)
else:
    os.waitpid(pid, 0)

# using execv() system call
pid = os.fork()
if pid == 0:
    os.execv("/bin/ls", ["/bin/ls", directory])
else:
    os.waitpid(pid, 0)

