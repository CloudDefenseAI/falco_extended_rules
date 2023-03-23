#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import subprocess

# Securely delete a file using shred
filename = "/home/f/syscall_analysis/ab"
subprocess.run(["shred", "-n", "3", "-vz", filename], check=True)
print(f"{filename} has been securely deleted.")

# Overwrite a block device with zeros using dd
device = "/dev/sdX"  # Replace X with the correct device letter
subprocess.run(["sudo", "dd", "if=/dev/zero", f"of={device}", "bs=1M"], check=True)
print(f"{device} has been overwritten with zeros.")

# Wipe free space on a mounted device using wipe
mountpoint = "/path/to/mounted/device"
subprocess.run(["wipe", "-kQqf", mountpoint], check=True)
print(f"Free space on {mountpoint} has been wiped securely.")

