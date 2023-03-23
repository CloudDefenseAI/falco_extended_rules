#!/usr/bin/env python
# coding: utf-8

# In[2]:


import socket
import struct

# Destination IP address and port
DEST_IP = "192.168.0.1"
DEST_PORT = 1234

# Create a raw socket
s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_RAW)

# Set the IP header fields
ip_version = 4
ip_header_length = 5  # 5 32-bit words
ip_tos = 0
ip_total_length = 20 + 8  # IP header + custom payload
ip_id = 0
ip_flags = 0
ip_ttl = 64
ip_protocol = socket.IPPROTO_TCP
ip_checksum = 0  # Will be calculated later
ip_src = socket.inet_aton("192.168.0.2")
ip_dst = socket.inet_aton(DEST_IP)

# Assemble the IP header
ip_header = struct.pack("!BBHHHBBH4s4s",
                        (ip_version << 4) + ip_header_length,  # Version and header length
                        ip_tos,  # Type of service
                        ip_total_length,  # Total length
                        ip_id,  # Identification
                        (ip_flags << 13),  # Flags and fragment offset
                        ip_ttl,  # Time to live
                        ip_protocol,  # Protocol
                        ip_checksum,  # Checksum (will be calculated later)
                        ip_src,  # Source IP address
                        ip_dst)  # Destination IP address

# Calculate the IP header checksum
ip_checksum = calculate_checksum(ip_header)
ip_header = struct.pack("!BBHHHBBH4s4s",
                        (ip_version << 4) + ip_header_length,  # Version and header length
                        ip_tos,  # Type of service
                        ip_total_length,  # Total length
                        ip_id,  # Identification
                        (ip_flags << 13),  # Flags and fragment offset
                        ip_ttl,  # Time to live
                        ip_protocol,  # Protocol
                        ip_checksum,  # Checksum
                        ip_src,  # Source IP address
                        ip_dst)  # Destination IP address

# Set the TCP header fields
tcp_src_port = 1234
tcp_dst_port = DEST_PORT
tcp_seq_num = 0
tcp_ack_num = 0
tcp_header_length = 5  # 5 32-bit words
tcp_flags = 2  # SYN flag
tcp_window_size = socket.htons(5840)  # Maximum amount of data the sender is willing to receive
tcp_checksum = 0  # Will be calculated later
tcp_urgent_pointer = 0

# Assemble the TCP header
tcp_header = struct.pack("!HHLLBBHHH",
                         tcp_src_port,  # Source port
                         tcp_dst_port,  # Destination port
                         tcp_seq_num,  # Sequence number
                         tcp_ack_num,  # Acknowledgment number
                         (tcp_header_length << 4),  # Data offset and reserved bits
                         tcp_flags,  # Control flags
                         tcp_window_size,  # Window size
                         tcp_checksum,  # Checksum (will be calculated later)
                         tcp_urgent_pointer)  # Urgent pointer

# Assemble the custom payload
payload = b"Hello, world!"

# Calculate the TCP pseudo-header for checksum calculation
tcp_pseudo_header = struct.pack("!4s4sBBH",
                                ip_src,  # Source IP address
                                ip_dst,)  # Destination IP


# In[ ]:




