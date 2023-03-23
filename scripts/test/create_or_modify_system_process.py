#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#!/usr/bin/env python3

import os

# Set the path to the Python script you want to execute
script_path = "/home/f/test/script_to_create_child_process_and_run_it.py"

# Set the name of the systemd service
service_name = "malicious1.service"

# Create the systemd service file
service_file = f"""[Unit]
Description=My service

[Service]
ExecStart=/usr/bin/python3 {script_path}
Restart=always

[Install]
WantedBy=multi-user.target
"""

# Write the service file to disk
service_path = f"/etc/systemd/system/{service_name}"
with open(service_path, "w") as f:
    f.write(service_file)

# Enable and start the systemd service
os.system(f"systemctl enable {service_name}")
os.system(f"systemctl start {service_name}")

