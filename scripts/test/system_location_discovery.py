#!/usr/bin/env python

import subprocess

# Obtain the network name and signal strength using nmcli
nmcli_command = "nmcli -f all device show wlan0"
nmcli_output = subprocess.check_output(nmcli_command.split()).decode()
network_name = None
signal_strength = None
for line in nmcli_output.split('\n'):
    if line.startswith('GENERAL.NAME:'):
        network_name = line.split(':')[1].strip()
    elif line.startswith('GENERAL.SIGNAL:'):
        signal_strength = line.split(':')[1].strip()
if network_name:
    print(f"Network name: {network_name}")
if signal_strength:
    print(f"Signal strength: {signal_strength}")

# Obtain the MAC address of the access point using iw
iw_command = "iw dev wlan0 link"
iw_output = subprocess.check_output(iw_command.split()).decode()
mac_address = None
for line in iw_output.split('\n'):
    if line.startswith('Connected to'):
        mac_address = line.split()[2]
if mac_address:
    print(f"MAC address: {mac_address}")

# Obtain the location of the network gateway using geoiplookup
ip_command = "ip route show | awk '/^default/{print $3}'"
ip_address = subprocess.check_output(ip_command.split()).decode().strip()
geoip_command = f"geoiplookup {ip_address}"
geoip_output = subprocess.check_output(geoip_command.split()).decode()
location_info = None
for line in geoip_output.split('\n'):
    if line.startswith('GeoIP City Edition'):
        location_info = line.split(',')[2].strip()
if location_info:
    print(f"Location info: {location_info}")

# Obtain the hostname of the system
hostname_command = "hostname"
hostname_output = subprocess.check_output(hostname_command.split()).decode().strip()
print(f"Hostname: {hostname_output}")

# Obtain the system's public IP address using curl and ipify.org
ipify_command = "curl https://api.ipify.org"
public_ip_address = subprocess.check_output(ipify_command.split()).decode().strip()
if public_ip_address:
    print(f"Public IP address: {public_ip_address}")

# Obtain the system's timezone using timedatectl
timedatectl_command = "timedatectl | grep Timezone | awk '{print $2}'"
timezone_output = subprocess.check_output(timedatectl_command.split()).decode().strip()
if timezone_output:
    print(f"Timezone: {timezone_output}")

# Obtain the system's latitude and longitude using geoclue2
geoclue_command = "geoclue2-lookup"
geoclue_output = subprocess.check_output(geoclue_command.split()).decode()
latitude = None
longitude = None
for line in geoclue_output.split('\n'):
    if line.startswith('Latitude='):
        latitude = line.split('=')[1].strip()
    elif line.startswith('Longitude='):
        longitude = line.split('=')[1].strip()
if latitude and longitude:
    print(f"Latitude: {latitude}")
    print(f"Longitude: {longitude}")

