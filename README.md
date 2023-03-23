### Falco rules by https://www.clouddefense.ai/
Curating Falco rules with MITRE ATT&amp;CK Matrix
https://attack.mitre.org/matrices/enterprise/cloud/

| Rule Name | Purpose | Corresponding Mitre |
| -------- | -------- | -------- |
|Account manipulation in ssh| account manipulation |Mitre Persistance|
|Suspicious Network Scanning Command|remote system discovery|Mitre Discovery|
|Suspicious Time and Date Command Execution|date,time and region discovery|Mitre Dscovery|
|Archive and Compression Activity|Archive Collected data|Mitre Collection|
|Detect peripheral device enumeration commands|Peripheral device discovery|Mitre Discovery|
|Detect service disable using systemctl|service stop|Mitre Impact|
|Chown or Chmod Operation|file and directory permission modification|Mitre Defense Evasion|
|Detect data destruction activity|Data destruction for impact|Mitre Impact|
|Read maps file of process|os credential dumping|Mitre Credential access|
|attempt to access bash history|unsecured credential access|Mitre Credential access|
|permission and group members discovery|permissions groups discovery|Mitre Discovery|
|system service discovery|To discover all services on a system|Mitre Discovery|
|boot or logon autostart execution|to detect if a script is embedded to execute on boot or logon|Mitre Persistance|
|Create accout or add user|to add a user to get persistance access of a system|Mitre Persistance|
|Create or Modify system process|to detect modified system process|Mitre Persistance|
|Create a system process which will execute a script |To detect creation of any malicious system service|Mitre Persistance|
|Credntials from password file|To detect reading sensitive password files present on system|Mitre Credential Access|
|Modify Authentication Process|To detetct any modifications done in asystems uthentication process|Mitre Credential Access|
|Process Injection|To detect any new process is embedded in to systems present process|Mitre Priviledge Escalation|
|Password policy discovery|To detect any discovery about set password policies of a system||

