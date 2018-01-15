"""
DESCRIPTION: retrieve and print the software information in a xml representation  from an vMX router with a REST API call. 
The rpc get-software-information is the equivalent of 'show version'
USAGE: python junos/get_software_information_in_xml.py
"""

import requests
from requests.auth import HTTPBasicAuth
from pprint import pprint

headers = { 'content-type' : 'application/xml' }
 
authuser = 'lab'
authpwd = 'm0naco'

r = requests.get('http://172.30.52.152:3000/rpc/get-software-information', auth=HTTPBasicAuth(authuser, authpwd), headers=headers)

# r.url
# r.status_code
# r.ok
# r.headers["Content-Type"]
# r.content

print r.content
