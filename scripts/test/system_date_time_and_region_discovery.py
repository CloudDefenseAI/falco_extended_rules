import subprocess

# Get current date and time
date_output = subprocess.check_output(['date', '+%Y-%m-%d %H:%M:%S'])
print("Current Date and Time:")
print(date_output.decode())

# Get time zone information
timedatectl_output = subprocess.check_output(['timedatectl', 'show', '-p', 'Timezone'])
timezone = timedatectl_output.decode().split('=')[1].strip()
print("Timezone:")
print(timezone)

# Get region information
locale_output = subprocess.check_output(['locale'])
region = locale_output.decode().split('=')[1].strip().split('.')[0]
print("Region:")
print(region)

# Get hostname information
hostnamectl_output = subprocess.check_output(['hostnamectl', 'status'])
hostname = hostnamectl_output.decode().split(' ')[3].strip()
print("Hostname:")
print(hostname)

