#!/usr/bin/env python
# coding: utf-8

# In[3]:


import subprocess

# Using the "ping" command
def ping(host):
    cmd = f"ping -c 1 {host}"
    return subprocess.call(cmd, shell=True) == 0

# Using the "nmap" command
def nmap_scan(network):
    cmd = f"nmap -sP {network}"
    output = subprocess.check_output(cmd, shell=True)
    return [line.split()[4] for line in output.decode().split("\n") if "Nmap scan report for" in line]

# Using the "arp" command
#def arp_scan():
 #   cmd = "arp -a"
  #  output = subprocess.check_output(cmd, shell=True)
   # return [line.split()[1][1:-1] for line in output.decode().split("\n") if len(line.split()) >= 4]

# Using the "host" command
def host_lookup(host):
    cmd = f"host {host}"
    output = subprocess.check_output(cmd, shell=True)
    return output.decode().split()[3]

# Using the "dig" command
def dig_lookup(host):
    cmd = f"dig +short {host}"
    output = subprocess.check_output(cmd, shell=True)
    return output.decode().strip()

# Using the "nslookup" command
def nslookup(host):
    cmd = f"nslookup {host}"
    output = subprocess.check_output(cmd, shell=True)
    return output.decode().split()[4]

if __name__ == '__main__':
    # Replace the parameters with the desired values
    host = "www.google.com"
    network = "10.0.2.15/24"

    if ping(host):
        print(f"{host} is up!")
    else:
        print(f"{host} is down.")

    print(f"Scanning network {network}...")
    hosts = nmap_scan(network)
    print(f"Found hosts: {hosts}")

    #arp_hosts = arp_scan()
    #print(f"ARP hosts: {arp_hosts}")

    print(f"Host lookup for {host}: {host_lookup(host)}")
    print(f"DIG lookup for {host}: {dig_lookup(host)}")
    print(f"NSLookup for {host}: {nslookup(host)}")


# In[ ]:





# In[ ]:




