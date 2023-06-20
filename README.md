
![CD-Logo](https://github.com/CloudDefenseAI/falco_extended_rules/assets/28846178/58bd666b-7a99-453e-a777-4a41bf789153)

## Falco rules hosted by CloudDefenseAI
https://attack.mitre.org/matrices/enterprise/cloud/ .
This repository contains a collection of extended [Falco](https://falco.org/) rules developed by CloudDefense.ai.

Falco is a powerful open-source behavioral activity monitor designed to detect and alert on unexpected application behavior in containers and Kubernetes. These extended rules provided by CloudDefense.ai enhance the default rule set and offer additional detection capabilities to strengthen the security of your containerized environment.

The image below shows the mitre attack coverage by Falco & extended coverage added by [Clouddefense.ai](https://www.clouddefense.ai/)

![MITRE_ATTACK_Updated](https://github.com/CloudDefenseAI/falco_extended_rules/assets/28846178/4c5147a1-647e-401e-99b5-5c00b36a15cc)



## Prerequisites
Before you begin, make sure you have the following prerequisites in place:

1. Falco Installed: Ensure that you have Falco installed on the target system where you want to enable runtime security. Refer to the official [Falco documentation](https://falco.org/docs/) for installation instructions.

2. Falco Configuration: Set up your Falco configuration file (falco.yaml) according to your specific needs. Make sure you have configured Falco to load external rule files.

## Installation
To install and use the extended rule set for Falco runtime security, follow these steps:

1. Clone the Repository: Start by cloning this GitHub repository to your local system: 
```
git clone https://github.com/CloudDefenseAI/falco_extended_rules.git
```
2. Navigate to the Repository: Change to the repository directory:
```
cd falco_extended_rules
```
3. Add Rules: Copy the extended rule files (custom_rules.yaml) from the cloned repository to a location accessible by Falco. For example, you can place them in the same directory as your Falco configuration file or in a separate directory, depending on your preference.
4. Update Falco Configuration: Open your Falco configuration file (falco.yaml) and add the following lines under the rules_file section:
```
   rules_file:
   -/path/to/your/rules/file1.yaml
   -/path/to/your/rules/file2.yaml
```
5. Restart Falco: Restart the Falco service to apply the changes and load the new rules.
```
# Restart Falco on systemd-based systems
sudo systemctl restart falco

# Restart Falco on non-systemd systems
sudo service falco restart
```   
##

### Below table shows the list of hosted rules in this repository: 

| S. No | Rule Name | Purpose | Corresponding Mitre |
| -------- | -------- | -------- | -------- |
|1|Account manipulation in ssh| account manipulation |Mitre Persistance|
|2|Suspicious Network Scanning Command|remote system discovery|Mitre Discovery|
|3|Suspicious Time and Date Command Execution|date,time and region discovery|Mitre Dscovery|
|4 |Archive and Compression Activity|Archive Collected data|Mitre Collection|
|5|Detect peripheral device enumeration commands|Peripheral device discovery|Mitre Discovery|
|6|Detect service disable using systemctl|service stop|Mitre Impact|
|7|Chown or Chmod Operation|file and directory permission modification|Mitre Defense Evasion|
|8|Detect data destruction activity|Data destruction for impact|Mitre Impact|
|9|Read maps file of process|os credential dumping|Mitre Credential access|
|10|attempt to access bash history|unsecured credential access|Mitre Credential access|
|11|permission and group members discovery|permissions groups discovery|Mitre Discovery|
|12|system service discovery|To discover all services on a system|Mitre Discovery|
|13|boot or logon autostart execution|to detect if a script is embedded to execute on boot or logon|Mitre Persistance|
|14|Create accout or add user|to add a user to get persistance access of a system|Mitre Persistance|
|15|Create or Modify system process|to detect modified system process|Mitre Persistance|
|16|Create a system process which will execute a script |To detect creation of any malicious system service|Mitre Persistance|
|17|Credntials from password file|To detect reading sensitive password files present on system|Mitre Credential Access|
|18|Modify Authentication Process|To detetct any modifications done in asystems uthentication process|Mitre Credential Access|
|19|Process Injection|To detect any new process is embedded in to systems present process|Mitre Priviledge Escalation|
|20|Password policy discovery|To detect any discovery about set password policies of a system||

The extended Falco rules included in this repository are carefully crafted and continuously updated by the experienced security experts at CloudDefense.ai. They address a wide range of potential security threats and anomalies, enabling you to identify suspicious activities, unauthorized access attempts, privilege escalations, and other malicious behaviors.

By leveraging these extended Falco rules, you can enhance your security posture, proactively monitor your containerized environment, and respond swiftly to any potential security incidents. Additionally, you have the flexibility to customize and fine-tune the rules according to your specific requirements and environment.

## Testing the Rules 
To ensure that the extended rules are functioning correctly, you can perform some test scenarios in your runtime environment. These can include simulating potential security events or actions that the rules are designed to detect. Monitor the Falco output, logs, or any configured alerting mechanism to observe the detection and response to these test scenarios.
## Contributing
If you want to help and wish to contribute, please review our contribution guidelines. Code contributions are always encouraged and welcome!
## Join the community
Join us on discord here, [#general](https://discord.gg/MyEJFm2hK7)
## License
This extended rule set for Falco runtime security is released under the [Apache-2.0 License](url).
## Disclaimer:

The content and code available in this GitHub repository are currently a work in progress. Please note that the rules, guidelines, or any other materials provided here are subject to change without prior notice.
While we aim to ensure the accuracy and completeness of the information presented, there may be errors or omissions. We kindly request users to exercise caution and critical judgment when utilizing or relying on any content found in this repository.
We appreciate your understanding and patience as we continue to develop and refine the content within this repository. Contributions, feedback, and suggestions are welcome and greatly valued, as they contribute to the ongoing improvement of this project.

