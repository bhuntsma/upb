#!/usr/bin/python
import urllib2
import json
from pprint import pprint
from datetime import datetime
#import xml.utils.iso8601

lat = 33.0109213
lng = -117.1405841

url = 'http://api.sunrise-sunset.org/json'
url += '?lat=' + str(lat)
url += '&lng=' + str(lng)
url += '&formatted=0'
url += '&date=today'

request = urllib2.Request(url)
response = urllib2.urlopen(request)
timestring = response.read()

info = json.loads(timestring)
pprint(info)

sunset = info['results']['sunset']
print sunset
#print info['civil_twilight_begin']
#print info['civil_twilight_end']

dt = datetime.strptime(sunset[:-6],"%Y-%m-%dT%H:%M:%S")
print dt
#print xml.utils.iso8601.parse(sunset)

#upb-cli --generate --net 163 --id 1 --type device --cmd activate --json --send -p /dev/ttyUSB0
#upb-cli --generate --net 163 --id 1 --type device --cmd deactivate --json --send -p /dev/ttyUSB0
