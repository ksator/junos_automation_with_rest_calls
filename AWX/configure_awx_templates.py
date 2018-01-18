'''
Usage: 
$ python AWX/configure_awx_templates.py 
run_pb.check.lldp.yml template has been created
run_pb.check.bgp.yml template has been created
run_pb.check.interfaces.yml template has been created
run_pb.check.vlans.yml template has been created
run_pb.check.lldp.json.yml template has been created
'''

import requests
from requests.auth import HTTPBasicAuth
import time
import sys
import json

authuser = 'admin'
authpwd = 'password'
headers = { 'content-type' : 'application/json' }
url = 'http://192.168.233.134/api/v2/job_templates/'

playbook_list = ['pb.check.lldp.yml', 'pb.check.bgp.yml', 'pb.check.interfaces.yml', 'pb.check.vlans.yml', 'pb.check.lldp.json.yml']

for item in playbook_list: 
 payload = {
     'name': "run_" + item, 
     'description': "template to execute " + item + " playbook", 
     'job_type': 'run', 
     'inventory': 2, 
     'project': 6, 
     'playbook': item, 
     'credential': 2, 
     'verbosity': 0, 
     "extra_vars": '', 
     "skip_tags": '', 
     "start_at_task": ''
 }
 rest_call = requests.post(url, headers=headers, auth=(authuser, authpwd), data=json.dumps(payload))
 # print rest_call.status_code
 if rest_call.status_code != 201: 
     print 'something went wrong with template for playbook ' + item
 else: 
     print 'run_' + item + 'template has been created'
 # print rest_call.json()

