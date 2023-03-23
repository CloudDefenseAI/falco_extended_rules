#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import time
import subprocess

# Run the script at the specified time
def run_script():
    subprocess.run(["python", "dummy.py"])

# Check the time every minute
while True:
    # Get the current time
    current_time = time.localtime()

    # Check if it's 5 o'clock
    if current_time.tm_hour == 5 and current_time.tm_min == 0:
        run_script()
    
    # Wait for a minute
    time.sleep(60)

