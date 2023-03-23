#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import subprocess

# Define the service name
service_name = "cups.service"

# Disable the service from starting at boot
subprocess.run(["sudo", "systemctl", "disable", service_name], check=True)

# Confirm that the service is disabled
output = subprocess.run(["sudo", "systemctl", "is-enabled", service_name], capture_output=True)
if output.stdout.strip() == b"disabled":
    print(f"The {service_name} service has been successfully disabled.")
else:
    print(f"Error: Failed to disable the {service_name} service.")

