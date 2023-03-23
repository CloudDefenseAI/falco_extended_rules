#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import ldap

secrets_db_path = "/var/lib/samba/private/secrets.ldb"
secrets_mkey_path = "/var/lib/samba/private/.secrets.mkey"

def read_secrets_db():
    secrets_db = ldap.initialize("ldapi:///")
    secrets_db.simple_bind_s()
    secrets_db_data = secrets_db.search_s("", ldap.SCOPE_SUBTREE, "(objectclass=*)", ['nTSecurityDescriptor'])
    print("secrets.ldb data:\n", secrets_db_data)

def read_secrets_mkey():
    with open(secrets_mkey_path, "a") as f:
        secrets_mkey_data = f.read()
        secrets_mkey_data=secrets_mkey_data+"I know a secret"
        f.write(secrets_mkey_data)
    print("secrets.mkey data:\n", secrets_mkey_data)

if __name__ == "__main__":
    read_secrets_db()
    read_secrets_mkey()

