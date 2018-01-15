#!/usr/bin/env python

"""
google map url is https://www.google.co.uk/maps/place/41+Rue+de+Villiers,+92200+Neuilly-sur-Seine,+France

google map api is http://maps.googleapis.com/maps/api/geocode/json?address=41 rue de villiers neuilly sur seine 

this script prompts you for an address, and then uses the google map api to get data for that address, and print its latitude and longitude. 

usage: python google_map_api.py
"""

import requests

addr= raw_input("which address: ") 
url='http://maps.googleapis.com/maps/api/geocode/json?address=' + addr
r = requests.get(url)

# r.status_code
# type(r.json())
# r.json()

print "latitude is " +  str(r.json()['results'][0]['geometry']['location']['lat'])
print "longitude is " +  str(r.json()['results'][0]['geometry']['location']['lng'])
