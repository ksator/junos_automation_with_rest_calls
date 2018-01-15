""" 
rest call to audit the state of bgp neighbors
usage: python junos/audit_bgp.py
"""

import requests
from pprint import pprint
from requests.auth import HTTPBasicAuth

my_headers = { 'Accept': 'application/json' }

ip = ["172.30.52.152", "172.30.52.153"]

for device in ip:
 uri = "http://" + device + ":8080/rpc/get-bgp-neighbor-information"
 r = requests.get(uri, auth=HTTPBasicAuth('lab', 'm0naco'), headers=my_headers)
 # print r.json()["bgp-information"][0]["bgp-peer"][0]["peer-state"][0]["data"]
 for item in  r.json()["bgp-information"]:
  print "**************************************************"
  print 'auditing bgp peers state for device ' + device
  print "session state for peer " + item["bgp-peer"][0]["peer-address"][0]["data"] + " is " + item["bgp-peer"][0]["peer-state"][0]["data"]

