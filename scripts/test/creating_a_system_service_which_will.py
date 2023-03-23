#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import os

# Define the contents of the service file
SERVICE_FILE = f"""\
[Unit]
Description=My Python Script

[Service]
Type=simple
ExecStart=/usr/bin/python {os.path.abspath('/home/f/test/execute_on_time_=5.py')}
WorkingDirectory={os.path.abspath('/home/f/test/')}
Restart=on-failure
User={os.getlogin()}

[Install]
WantedBy=multi-user.target
"""

# Write the service file to disk
with open('/etc/systemd/system/my_python_script.service', 'w') as f:
    f.write(SERVICE_FILE)
    f.close()

# Enable the service
os.system('systemctl enable my_python_script.service')

