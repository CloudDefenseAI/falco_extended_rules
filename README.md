
![CD-Logo](https://github.com/CloudDefenseAI/falco_extended_rules/assets/28846178/58bd666b-7a99-453e-a777-4a41bf789153)

## Falco rules hosted by CloudDefenseAI
https://attack.mitre.org/matrices/enterprise/cloud/ .
This repository contains a collection of extended [Falco](https://falco.org/) rules developed by CloudDefense.ai.

Falco is a powerful open-source behavioral activity monitor designed to detect and alert on unexpected application behavior in containers and Kubernetes. These extended rules provided by CloudDefense.ai enhance the default rule set and offer additional detection capabilities to strengthen the security of your containerized environment.

The image below shows the mitre attack coverage by Falco & extended coverage added by [Clouddefense.ai](https://www.clouddefense.ai/)


![kkkk](https://github.com/CloudDefenseAI/falco_extended_rules/assets/28846178/0f490715-8d74-4950-8b2b-5baf54d870db)



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
|2|Suspicious disk activity|Detects disk wiping, overwriting or corrupting raw disk data|Mitre Impact|
|3|Disable Recovery Features|Dtects disabling of system recovery features|Mitre Impact|
|4|Detect Data Destruction Activity|Detects activity related to data destruction|Mitre Imapct|
|5|Suspicious Network Scanning Command|Detects suspicious network scanning commands|Mitre Discovery|
|6|Permission and Group Members Discovery|Detects permission of files and group and its group members|Mitre Discovery|
|7|Detect Peripheral Device Enumeration Commands|Detects if someone runs commands that enumerate peripheral devices|Mitre Discovery|
|8|Suspicious Time and Date Command Execution|Detects the execution of commands that may be used to gather time, date, and region information|Mitre Discovery|
|9|Enumerate Domain Trusts|Detects attempts to enumerate domain trusts in Linux systems|Mitre Discovery|
|10|Detect System Location Information Retrieval|Detects attempts to retrieve system information|Mitre Discovery|
|11|Get Information About Open Application Windows|Detects attempts to get information about open application windows|Mitre Discovery|
|12|Suspicious System Information Gathering|Detects suspicious commands related to gathering system information|Mitre Discovery|
|13|Read Maps File of Process|An attempt to read the maps file of a process will be detected|Mitre Credential Access|
|14|Attempt to Access Bash History File|Someone is attempting to access the bash history file|Mitre Credential Access|
|15| Chown or Chmod Operation|Detects chown or chmod operations|Mitre Defense Evasion|
|16|Execute Command Via Utility|Detects execution of commands via parse text, scripting languages, and system utilities|Mitre Defense Evasion|
|17|Read Disk Block Command|Detects execution of commands that read disk blocks|Mitre Defense Evasion|
|18|Archive and Compression Activity|Detects archive and compression activity using tar, zip, gzip, and bzip2|Mitre Collection|
|19|Detect Service Disable Using Systemctl|Detect Service Disable Using Systemctl|Mitre Impact|
|20|System Service Discovery|an attempt to discover all services that are running in system|Mitre Discovery|



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

