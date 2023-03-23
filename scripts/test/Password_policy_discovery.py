#!/usr/bin/env python
# coding: utf-8

# In[2]:





# In[4]:


import pam

# Define the PAM service to use for authentication
PAM_SERVICE = "pwquality.conf"

# Create a new PAM instance
p = pam.pam()

# Define a dictionary to store the password policies
password_policies = {}

# Get the password policies from the PAM configuration
pam_config = open("/etc/security/" + PAM_SERVICE, "r").readlines()
for i in pam_config:
    print(i)
for line in pam_config:
    line = line.strip()
    if line.startswith("password"):
        words = line.split()
        if "required" in words:
            if "minlen=" in words:
                password_policies["min_length"] = int(words[words.index("minlen=")+1])
            if "dcredit=" in words:
                password_policies["min_digit"] = int(words[words.index("dcredit=")+1])
            if "ucredit=" in words:
                password_policies["min_uppercase"] = int(words[words.index("ucredit=")+1])
            if "lcredit=" in words:
                password_policies["min_lowercase"] = int(words[words.index("lcredit=")+1])
            if "ocredit=" in words:
                password_policies["min_special_chars"] = int(words[words.index("ocredit=")+1])
            if "maxrepeat=" in words:
                password_policies["max_repeat"] = int(words[words.index("maxrepeat=")+1])
            if "minclass=" in words:
                password_policies["min_character_classes"] = int(words[words.index("minclass=")+1])
            if "remember=" in words:
                password_policies["password_history"] = int(words[words.index("remember=")+1])

# Print the password policies
print(password_policies)


# In[ ]:




