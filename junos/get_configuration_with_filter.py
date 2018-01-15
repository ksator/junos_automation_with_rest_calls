"""
DESCRIPTION: retrieve a subset of the Junos configuratiom in a xml representation from an vMX router with a REST API call, and print it.  
USAGE: python junos/get_configuration_with_filter.py
"""

import requests
from requests.auth import HTTPBasicAuth
from pprint import pprint

headers = { 'content-type' : 'application/xml' }
 
#indicate below the device credentials 
authuser = 'lab'
authpwd = 'm0naco'

# the default port for junos rest api is 3000. I am using the port 8080 for this device 

# get the junos configuration with a filter

payload = ('<get-config><source><running/></source><filter type="subtree"><configuration><interfaces><interface><name>ge-0/0/0</name></interface></interfaces></configuration></filter></get-config>')

q = requests.post('http://172.30.52.152:8080/rpc', headers=headers, auth=HTTPBasicAuth(authuser, authpwd), data=payload)

print q.content
