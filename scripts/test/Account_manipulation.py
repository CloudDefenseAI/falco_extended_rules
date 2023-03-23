#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import os

# Path to authorized_keys file
authorized_keys_path = '/home/f/.ssh/authorized_keys'

# Path to sshd_config file
sshd_config_path = '/etc/ssh/sshd_config'

# Add a new public key to authorized_keys file
with open(authorized_keys_path, 'a') as f:
    f.write('\nssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQC3dY6Z5g6xP+oLW8I3qCvbBUmJyvzCZ68W8QXzjKbP7SKvT35B+T8TJ01fgTb1yBv1Iucb+p8SEtPZoMnZcT0GbdT+T8Dyghya1y2K1tD0WzsI8WsXJ+rAVZcYwbxH+lr0hs8qF3CqPYEJ+LzC1f2PN9uxzGZbLO/t4vNbuB4QFbG6NnyjjRwKIFzoDlUJ8qU6Y5U6Z1xZOJjK6eP/ZmFZHmC+JvMcNVdwTXK7zX/s+tsW8FpzMQV7h9bUS+spUC7xEum8PshPKmJj+TlRJ0m8ZzWox6ZWbjF6+dc2sJQb6xFq2aC+Dx00uVg4z8F84W+7PNPOmnUSX9VYoSv8ouYofwA5SKxJx/W/B+IvPnlfDQHdx2XrX9rI5g5rE45XTzGJiLhqIPQcglXX8qAqJqwVKaRLnX9Rz/Xn1/xYLeEVwzEDx22a0rbLVaG3ZK3OJzutn0iXlRm0jKpYbLfUKi81xOvr/5dwnZ0I04i2GtquH9Xr5rB/l5Yt7PDM= user@host\n')
    f.close()

# Modify the sshd_config file to disable root login and password authentication
with open(sshd_config_path, 'r') as f:
    config_lines = f.readlines()
    f.close()

# Replace the line containing "PermitRootLogin" with a new line that disables root login
for i in range(len(config_lines)):
    if 'PermitRootLogin' in config_lines[i]:
        config_lines[i] = 'PermitRootLogin no\n'

# Replace the line containing "PasswordAuthentication" with a new line that disables password authentication
for i in range(len(config_lines)):
    if 'PasswordAuthentication' in config_lines[i]:
        config_lines[i] = 'PasswordAuthentication no\n'

# Write the modified sshd_config file back to disk
with open(sshd_config_path, 'w') as f:
	f.writelines(config_lines)
	f.close()

