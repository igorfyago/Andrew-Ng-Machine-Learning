#ASSIGNMENT WEEK 5
import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter location: ')
if len(url) < 1: url = 'http://py4e-data.dr-chuck.net/comments_101232.xml'
print('Retrieving', url)

xml = urllib.request.urlopen(url, context=ctx).read()
# This is an object:
tree = ET.fromstring(xml)
#This is a list of objects:
tags = tree.findall('comments/comment')
print('Length tags:', len(tags))

add = 0
for tag in tags:
    print('Count is ', tag.find('count').text)
    add = add + int(tag.find('count').text)
print('Sum:', add)
