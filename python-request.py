# These two commands solve the issue of HTTPS InsecurePlatformWarning in Python:
# pip install requests
# pip install pyopenssl ndg-httpsclient pyasn1

import requests, json
import requests.packages.urllib3.contrib.pyopenssl
requests.packages.urllib3.contrib.pyopenssl.inject_into_urllib3()

headers = {'content-type': 'application/vnd.api+json', 'accept': 'application/*, text/*', 'x-api-key': 'feWf7yUc5vec3oD7A'}
r = requests.get('https://api.tnyu.org/v2/events', headers=headers)
data = json.loads(r.text)

# All events
# print data['data']

# Title of the first event that's returned from the API
# print data['data'][0]['title']

# Printing out all the titles
for i in data['data']:
	print i['title']
