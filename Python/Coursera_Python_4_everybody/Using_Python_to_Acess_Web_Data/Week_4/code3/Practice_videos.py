#DESCARGAR UNA IMAGEN 😌:
#import socket
#import time

#HOST = 'surgeryvip.com'
#PORT = 80

#no usamos el .read cuando creamos sockets (es decir, cuando hacemos el request manualmente)
#mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#mysock.connect((HOST, PORT))
#mysock.sendall(b'GET https://surgeryvip.com/wp-content/uploads/2015/04/megan-fox-gq2-year-01.jpg HTTP/1.0\r\n\r\n')
#count = 0
#picture = b''

#while True:
    #data = mysock.recv(5120)
    #if len(data) < 1: break
    #time.sleep(0.000001)
    #count = count + len(data)
    #print(len(data), count)
    #picture = picture + data #(concatena el espacio '' con la nueva info y con la b delante la convierte en binaria)

#mysock.close()

#We only want the data that form the image, so we use find to slice to skip the header and we decodify the header before printing:
#pos = picture.find(b'\r\n\r\n')
#print('Header length', pos)
#print(picture[:pos].decode()) #Aqui decodificamos esta parte, porque al no formar parte de la imagen, no tiene caracteres raros y no sale error.
#now we know \r is the position, so we add +4 to get all the data past the header and we keep the picture in binary, codified:

#picture = picture[pos+4:]
#fhand = open('image.jpg', 'wb')
#fhand.write(picture)
#fhand.close()





#FORMA CORTA DE GUARDAR UNA IMAGEN USANDO URLLIB😉:
#Cuando usamos el .read es porque no tenemos pensado usar un forloop o un while loop para trabajar con la info.
#En este caso guardamos la imagen del tiron, sin while loops y usamos toda la memoria disponible del mac:
#import urllib.request, urllib.parse, urllib.error

#img = urllib.request.urlopen('http://data.pr4e.org/cover3.jpg').read()
#fhand = open('cover3.jpg', 'wb')
#fhand.write(img)
#fhand.close()

#La otra forma es usar while loop para sacar la informacion por bloques para no chupar toda la memoria😀:

#import urllib.request, urllib.parse, urllib.error
#img = urllib.request.urlopen('http://data.pr4e.org/cover3.jpg')
#fhand = open('cover3.jpg', 'wb')
#size = 0
#while True:
#    data = img.read(100000)
#    if len(data) < 1 : break
#    size = size + len(data)
#    fhand.write(data)
#print(size,'Characters added')
#fhand.close()





#HOW TO FIND WITH REGEX IN SECURE PAGES😀 :
#import urllib.request, urllib.parse, urllib.error
#import re
#import ssl

# Ignore SSL certificate errors (Para poder entrar en webs seguras)
#ctx = ssl.create_default_context()
#ctx.check_hostname = False
#ctx.verify_mode = ssl.CERT_NONE

#Retrieve with regex
#url = input('Enter url')
#if len(url) < 1 : url = 'http://www.dr-chuck.com/page1.htm'
#html = urllib.request.urlopen(url).read()
#links = re.findall(b'href="(http[s]?://.*?)"', html)
#for link in links:
#    print(link.decode())





#MOST OF THE TIME REGEX DO NOT WORK ON FLAWED HTML, THAT'W SHY WE USE BEAUTIFULSOUP, IT TAKES CARE OF PUTTING DATA ON A NICE WAY😍:
#import urllib.request, urllib.parse, urllib.error
#import ssl
#from bs4 import BeautifulSoup

#ignore the ssl
#ctx = ssl.create_default_context()
#ctx.check_hostname = False
#ctx.verify_mode = ssl.CERT_NONE


#url = input('Enter url',)
#if len(url) < 1 : url = 'http://www.dr-chuck.com/page1.htm'
#html = urllib.request.urlopen(url, context=ctx).read()
#soup = BeautifulSoup(html, 'html.parser')
#tags = soup('a')
#Retrieve all the anchor tags (hipervinculos):
#for tag in tags:
    #print('TAG:', tag)
    #print('URL:', tag.get('href', None))
    #print('Contents:', tag.contents[0])
    #print('Attrs:', tag.attrs)





#ASSIGNMENT SCRAPPING HTML DATA😍:

#import urllib.request, urllib.parse, urllib.error
#import ssl
#from bs4 import BeautifulSoup

#ctx = ssl.create_default_context()
#ctx.check_hostname = False
#ctx.verify_mode = ssl.CERT_NONE

#url = input('Enter -')
#if len(url) < 1 : url = 'http://py4e-data.dr-chuck.net/comments_101230.html'
#html = urllib.request.urlopen(url, context=ctx).read()
#soup = BeautifulSoup(html, 'html.parser')
#tags = soup('span')

#retrieve the tags and sum the numbers:
#add = 0
#count = 0
#for tag in tags:
    #print('TAG:', tag)
    #print('Content:', tag.contents[0])
    #num = int(tag.contents[0])
    #add = add + num
    #count = count + 1
#print(count, add)





#ASSIGNMENT FOLLOWING LINKS IN HTML😎:

import urllib.request, urllib.parse, urllib.error
import ssl
from bs4 import BeautifulSoup

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter url')
if len(url) < 1 : url = 'http://py4e-data.dr-chuck.net/known_by_Schuyler.html'
while True:
    count = input('Enter nº of websites to scrap ')
    try:
        count = int(count)
        break
    except:
        print('Invalid input')
        continue
while True:
    pos = input('Enter nº of link position ')
    try:
        pos = int(pos)
        break
    except:
        print('Enter a valid number')
        continue

while count > 0:
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    url = tags[pos].get('href', None)
    count = count - 1
    for tag in tags[pos]:
        print('TAG:', tag)






#https://www.tuaceitedemotor.com
#python3 Practice_videos.py
#cd Desktop/Aitor/Coursera/Python/Using_Python_to_Acess_Web_Data/Week_4/code3
