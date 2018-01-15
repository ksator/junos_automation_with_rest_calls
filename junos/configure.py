""" 
rest call to configure junos 
usage: python junos/configure.py
"""

import requests
from requests.auth import HTTPBasicAuth
from pprint import pprint

headers = { 'content-type' : 'application/xml' }
authuser = 'lab'
authpwd = 'm0naco'

payload = ("<lock-configuration/><load-configuration><configuration><system><login><message>welcome to REST demo</message></login></system></configuration></load-configuration><commit/><unlock-configuration/>")

url = 'http://172.30.52.152:8080/rpc'

q = requests.post(url, headers=headers, auth=(authuser, authpwd), data=payload)

print q.status_code

"""
lab@dc-vmx-3> show system commit
0   2018-01-15 12:38:45 UTC by lab via junoscript
"""
