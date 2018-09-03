#Así es como se empieza, para saber como se hacen los sockets. Mas adelante usaremos urllib.request que lo hace automaticamente.
#make the conection (socket):
import socket
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))

#how to make a get request:
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)
#it encodes to a format called utfa and sends it
#now the server do a bucnh of staff and send us back some info. We do a while loop to receive that info:
#and we decode that utfa to unicode which is an internal code
while True:
    data = mysock.recv(20)
    if len(data) < 1: break
    print(data.decode(),end='')
mysock.close()


#cd Desktop/Aitor/Coursera/Python/Using_Python_to_Acess_Web_Data/Week_3
#python3 Hyper_Text_Transfer_Protocol.py
