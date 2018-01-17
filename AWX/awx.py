'''
usage: 
$ python AWX/awx.py <template_name>

example: 
$ python AWX/awx.py wrong_name
there is a problem with that template

example: 
$ python AWX/awx.py valid_name
waiting for the job to complete ... 
still waiting for the job to complete ...
still waiting for the job to complete ...
status is successful
'''

import requests
from requests.auth import HTTPBasicAuth
# from pprint import pprint
import time
import sys

# make sure this user has permission to execute this AWX template
authuser = 'admin'
authpwd = 'password'

# rest call to run the AWX template
headers = { 'content-type' : 'application/json' }
payload = {}
template_name = sys.argv[1]
url = 'http://192.168.233.134/api/v2/job_templates/' + template_name + '/launch/'
rest_call = requests.post(url, headers=headers, auth=(authuser, authpwd), data=payload)

# print 'rest call http response code is ' + str(rest_call.status_code)
# expected value for rest_call.status_code is 201
if rest_call.status_code !=201: 
  print "there is a problem with that template"
  sys.exit()

print "waiting for the job to complete ... "
time.sleep(15)

# print 'job that have the details for the previous rest call is ' + str(rest_call.json()['job'])
# rest call to get the status of the previous template execution
url='http://192.168.233.134/api/v2/jobs/' + str(rest_call.json()["job"])
headers = { 'Accept' : 'application/json' }
status=requests.get(url, auth=(authuser, authpwd), headers=headers)

# waiting for the job to complete, and then print the job status
while status.json()["status"] not in ["successful","failed"]:
  print "still waiting for the job to complete ..."
  time.sleep(15)
  status=requests.get(url, auth=(authuser, authpwd), headers=headers)
print "status is " + status.json()["status"]

