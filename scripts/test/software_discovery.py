import subprocess

# List all installed packages and their versions using dpkg
print('List of installed packages and their versions:')
dpkg_process = subprocess.Popen(['dpkg', '-l'], stdout=subprocess.PIPE)
output, error = dpkg_process.communicate()
print(output.decode())

# Display information about the Ubuntu distribution
print('Information about the Ubuntu distribution:')
lsb_process = subprocess.Popen(['lsb_release', '-a'], stdout=subprocess.PIPE)
output, error = lsb_process.communicate()
print(output.decode())

# Display the version number of the Ubuntu kernel
print('Version number of the Ubuntu kernel:')
uname_process = subprocess.Popen(['uname', '-r'], stdout=subprocess.PIPE)
output, error = uname_process.communicate()
print(output.decode())

# List the files in the /usr/bin directory and their versions
print('List of files in /usr/bin directory and their versions:')
ls_process = subprocess.Popen(['ls', '-l', '/usr/bin'], stdout=subprocess.PIPE)
output, error = ls_process.communicate()
print(output.decode())

