import urllib.request, urllib.parse, urllib.error
import json

url = input('Enter url:')
if len(url) < 1 : url = 'http://py4e-data.dr-chuck.net/comments_101233.json '

data = urllib.request.urlopen(url).read()
print('Retrieving:', url)

js = json.loads(data)
print('User count:', len(js))
print(json.dumps(js, indent=4))

add = 0
for item in js['comments']:
    add = add + int(item['count'])
    print(item['count'], add)

#for item in info:
    #print('Name', item['name'])
    #print('Id', item['id'])
    #print('Attribute', item['x'])
