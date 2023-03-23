#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#!/usr/bin/env python3

import os

# Set the path to the Python script you want to execute
script_path = "dummy.py"

# Use os.fork() to create a new process
pid = os.fork()

# If pid is 0, we're in the child process
if pid == 0:
    # Use os.execvp() to replace the child process with the Python interpreter running the script
    os.execvp("python3", ["python3", script_path])

# If pid is not 0, we're in the parent process
else:
    # Print the child process's PID
    print(f"Child process created with PID {pid}")

