import requests
from requests.auth import HTTPBasicAuth

authuser = 'admin'
authpwd = 'password'
url = 'http://192.168.233.134/api/v2/job_templates/13'
rest_call = requests.delete(url, auth=(authuser, authpwd))

