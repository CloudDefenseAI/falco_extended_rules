#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import subprocess

# Define the PAM configuration file path
pam_config_file = "/etc/pam.d/common-auth"

# Add a new authentication module to the PAM configuration
subprocess.run(["sudo", "sed", "-i", "s/^auth\s*required\s*pam_unix.so$/auth required pam_unix.so\nauth required pam_mymodule.so/", pam_config_file])

# Remove an existing authentication module from the PAM configuration
subprocess.run(["sudo", "sed", "-i", "/^auth\s*required\s*pam_permit.so/d", pam_config_file])

# Modify an existing authentication module in the PAM configuration
subprocess.run(["sudo", "sed", "-i", "s/^auth\s*required\s*pam_deny.so$/auth required pam_deny.so debug/", pam_config_file])


# In[ ]:


import fileinput

# Open the common-auth file for editing
with fileinput.FileInput("/etc/pam.d/common-auth", inplace=True) as file:

    # Iterate over each line in the file
    for line in file:

        # If the line contains "auth sufficient pam_unix.so", replace it with "auth sufficient pam_unix.so my_custom_module.so"
        if "auth sufficient pam_unix.so" in line:
            print(line.replace("auth sufficient pam_unix.so", "auth sufficient pam_unix.so my_custom_module.so"))

        # If the line contains "auth [success=1 default=ignore] pam_unix.so", replace it with "auth [success=1 default=ignore] pam_unix.so my_custom_module.so"
        elif "auth [success=1 default=ignore] pam_unix.so" in line:
            print(line.replace("auth [success=1 default=ignore] pam_unix.so", "auth [success=1 default=ignore] pam_unix.so my_custom_module.so"))

        # Otherwise, print the line as-is
        else:
            print(line, end="")

