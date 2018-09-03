import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

serviceurl = 'http://maps.googleapis.com/maps/api/geocode/xml?'

while True:
    address = input('Enter location: ')
    if len(address) < 1: break

    url = serviceurl + 'address='+address#urllib.parse.urlencode({'address': address})
    print('Retrieving', url)
    fhand = urllib.request.urlopen(url).read()
    print('Retrieved', len(fhand), 'characters')
    print(fhand.decode())
    tree = ET.fromstring(fhand)

    results = tree.findall('result')
    lat = results[0].find('geometry').find('location').find('lat').text
    lng = results[0].find('geometry').find('location').find('lng').text
    location = results[0].find('formatted_address').text

    print('lat', lat, 'lng', lng)
    print(location)
