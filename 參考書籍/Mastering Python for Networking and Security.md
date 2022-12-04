## [Mastering Python for Networking and Security - Second Edition](https://www.packtpub.com/product/mastering-python-for-networking-and-security-second-edition/9781839217166)
- [GITHUB](https://github.com/PacktPublishing/Master-Math-by-Coding-in-Python)

## content
```
Section 1: The Python Environment and System Programming Tools
Chapter 1: Working with Python Scripting
Chapter 2: System Programming Packages

Section 2: Network Scripting and Extracting Information from the Tor Network with Python
Chapter 3: Socket Programming
Chapter 4: HTTP Programming
Chapter 5: Connecting to the Tor Network and Discovering Hidden Services

Section 3: Server Scripting and Port Scanning with Python
Chapter 6: Gathering Information from Servers
Chapter 7: Interacting with FTP, SFTP, and SSH Servers
Chapter 8: Working with Nmap Scanner

Section 4: Server Vulnerabilities and Security in Python Modules
Chapter 9: Interacting with Vulnerability Scanners
Chapter 10: Identifying Server Vulnerabilities in Web Applications
Chapter 11: Security and Vulnerabilities in Python Modules

Section 5: Python Forensics
Chapter 12: Python Tools for Forensics Analysis
Chapter 13: Extracting Geolocation and Metadata from Documents, Images, and Browsers
Chapter 14: Cryptography and Steganography
Assessments
```
## 
- [The Shodan RESTful API](https://developer.shodan.io/api)
```python
#!/usr/bin/env python
import requests
import os
SHODAN_API_KEY = os.environ['SHODAN_API_KEY']
ip = '1.1.1.1'
def ShodanInfo(ip):
    try:
        result = requests.get(f"https://api.shodan.io/shodan/host/{ip}?key={SHODAN_API_KEY}&minify=True").json()
    except Exception as exception:
        result = {"error":"Information not available"}
    return result
print(ShodanInfo(ip))
```
- Shodan search with Python
```python
#!/usr/bin/python
import shodan
import os
SHODAN_API_KEY = os.environ['SHODAN_API_KEY']
shodan = shodan.Shodan(SHODAN_API_KEY)
try:
    resultados = shodan.search('nginx')
    print("results :",resultados.items())
except Exception as exception:
    print(str(exception))
```
- 撰寫具規格的程式 shodanSearch.py
```python
$ python3 shodanSearch.py -h
usage: shodanSearch.py [-h] [--target TARGET] [--search SEARCH]
Shodan search
optional arguments:
  -h, --help      show this help message and exit
  --target TARGET  target IP / domain
  --search SEARCH  search
```
```python
#!/usr/bin/env python

import shodan
import argparse
import socket
import sys
import os

SHODAN_API_KEY = os.environ['SHODAN_API_KEY']

api = shodan.Shodan(SHODAN_API_KEY)

parser = argparse.ArgumentParser(description='Shodan search')

parser.add_argument("--target", dest="target", help="target IP / domain", required=None)
parser.add_argument("--search", dest="search", help="search", required=None)

parsed_args = parser.parse_args()

if len(sys.argv)>1 and sys.argv[1] == '--search':
    try:
        results = api.search(parsed_args.search)
        print('Results: %s' % results['total'])
        for result in results['matches']:
            print('IP: %s' % result['ip_str'])
            print(result['data'])
    except shodan.APIError as exception:
        print('Error: %s' % exception)
        
if len(sys.argv)>1 and sys.argv[1] == '--target':
    try:
        hostname = socket.gethostbyname(parsed_args.target)
        results = api.host(hostname)
        print("""
                IP: %s
                Organization: %s
                Operating System: %s
        """ % (results['ip_str'], results.get('org', 'n/a'), results.get('os', 'n/a')))

        for item in results['data']:
            print("""Port: %s Banner: %s""" % (item['port'], item['data']))
        
    except shodan.APIError as exception:
        print('Error: %s' % exception) 
```
# Section 5: Python Forensics
## Chapter 12: Python Tools for Forensics Analysis
- chapter12/registry/get_information_operating_system.py
```python
#!/usr/bin/python3

import sys
from Registry import Registry
reg = Registry.Registry(sys.argv[1])

print("Analyzing SOFTWARE in Windows registry...")

try:
    key = reg.open("Microsoft\\Windows NT\\CurrentVersion")
    print("\tProduct name: " + key.value("ProductName").value())
    print("\tCurrentVersion: " + key.value("CurrentVersion").value())
    print("\tServicePack: " + key.value("CSDVersion").value())
    print("\tProductID: " + key.value("ProductId").value() + "\n")
except Registry.RegistryKeyNotFoundException as exception:
    print("Exception",exception)
```
- chapter12/registry/get_information_services.py
```python
#!/usr/bin/python3

from Registry import Registry
import sys

def getCurrentControlSet(registry):
    try:
        key = registry.open("Select")
        for value in key.values():
            if value.name() == "Current":
                return value.value()
    except Registry.RegistryKeyNotFoundException as exception:
        print("Couldn't find SYSTEM\Select key ",exception)

def getServiceInfo(dictionary):
    serviceType = { 1 : "Kernel device driver", 2 : "File system driver", 4 : "Arguments for an adapter",
    8 : "File system driver interpreter", 16 : "Own process", 32 : "Share process",272 : "Independent interactive program",
    288 : "Shared interactive program" }
    print(" Service name: %s" % dictionary["SERVICE_NAME"])
    if "DisplayName" in dictionary:
        print (" Display name: %s" % "".join(dictionary["DisplayName"]).encode('utf8'))

    if "ImagePath" in dictionary:
        print(" ImagePath: %s" % dictionary["ImagePath"])

    if "Type" in dictionary:
        print(" Type: %s" % serviceType[dictionary["Type"]])

    if "Group" in dictionary:
        print(" Group: %s" % dictionary["Group"])

    print("--------------------------")


def serviceParams(subkey):
    service = {}
    service["SERVICE_NAME"] = subkey.name()
    service["ModifiedTime"] = subkey.timestamp()

    for value in subkey.values():
        service[value.name()] = value.value()

    getServiceInfo(service)

def servicesKey(registry, controlset):
    serviceskey = "ControlSet00%d\\Services" % controlset
    try:
        key = registry.open(serviceskey)
    except Registry.RegistryKeyNotFoundException as exception:
        print("Couldn't find Services key ",exception)

    for subkey in key.subkeys():
        serviceParams(subkey)


if __name__ == "__main__" :
    registry = Registry.Registry(sys.argv[1])
    controlset = getCurrentControlSet(registry)
    servicesKey(registry, controlset)
```
- chapter12/registry/get_registry_information.py
```python
#!/usr/bin/python3

import sys
from Registry import Registry
reg = Registry.Registry(sys.argv[1])

print("Analyzing SOFTWARE in Windows registry...")

try:
    key = reg.open("Microsoft\\Windows\\CurrentVersion\\Run")
    print("Last modified: %s [UTC]" % key.timestamp())
    for value in key.values():
            print("Name: " + value.name() + ", Value path: " + value.value())
except Registry.RegistryKeyNotFoundException as exception:
    print("Exception",exception)
```
## Chapter 13: Extracting Geolocation and Metadata from Documents, Images, and Browsers
## Chapter 14: Cryptography and Steganography
