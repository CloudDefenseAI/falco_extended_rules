#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#!/usr/bin/env python3

import os

# Set the path to the program you want to run
program_path = "/home/f/test/dummy.py"

# Set the name of the systemd service
service_name = "malicious.service"

# Create the systemd service file
service_file = f"""[Unit]
Description=My program
After=network.target

[Service]
WorkingDirectory=/home/f/test/
ExecStart=/usr/bin/python3 {program_path}
Restart=always

[Install]
WantedBy=default.target
"""

# Write the service file to disk
service_path = f"/etc/systemd/system/{service_name}"
with open(service_path, "w") as f:
    f.write(service_file)
    f.close()

# Enable and start the systemd service
os.system(f"systemctl --user enable {service_name}")
os.system(f"systemctl --user start {service_name}")

