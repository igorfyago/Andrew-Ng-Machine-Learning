import urllib.request, urllib.parse, urllib.error
import json

# Note that Google is increasingly requiring keys
 #for this API
serviceurl = 'http://maps.googleapis.com/maps/api/geocode/json?'

while True:
    address = input('Enter location: ')
    if len(address) < 1: break

    url = serviceurl + urllib.parse.urlencode({'address': address})

    print('Retrieving', url)
    fhand = urllib.request.urlopen(url).read().decode()
    print('Retrieved', len(fhand), 'characters')

    try:
        js = json.loads(fhand)
    except:
        js = None

    if not js or 'status' not in js or js['status'] != 'OK':
        print('==== Failure To Retrieve ====')
        print(fhand)
        continue

    print(json.dumps(js, indent=4))

    lat = js["results"][0]["geometry"]["location"]["lat"]
    lng = js["results"][0]["geometry"]["location"]["lng"]
    print('lat', lat, 'lng', lng)
    location = js['results'][0]['formatted_address']
    print(location)

    #python3 geojson.py
    #cd Desktop/Aitor/Coursera/Python/Using_Python_to_Acess_Web_Data/Week_6/code3
