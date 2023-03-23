#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from scapy.all import *

def packet_callback(packet):
    print(packet.summary())

sniff(prn=packet_callback,filter= "tcp", count=10)

