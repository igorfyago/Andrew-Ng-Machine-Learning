import urllib.request, urllib.parse, urllib.error
import json
import ssl

serviceurl = 'http://py4e-data.dr-chuck.net/geojson?'

while True:
    address = input('Enter Location:')
    if len(address) < 1 : break

    url = serviceurl + urllib.parse.urlencode({'address': address})
    print('Retrieving:', url)
    data = urllib.request.urlopen(url).read()
    print('Retrieved', len(data), 'Characters')

    js = json.loads(data)
    print(json.dumps(js, indent=4))

    print('Retrieve', js['results'][0]['place_id'])
