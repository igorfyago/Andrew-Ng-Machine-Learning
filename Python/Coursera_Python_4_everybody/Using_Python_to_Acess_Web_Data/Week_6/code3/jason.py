import json

data = '''{"name" : "Chuck",
   "phone" :{"type" : "intl",
    "number" : "+1 734 303 4456"
   }, "email" : {"hide" : "yes"
   }
 }'''

#en este caso crea literalmente un diccionario en python. Si empezara por [] crearia una lista
info = json.loads(data)
#la unica diferencia es que tenemos que poner el value entrecomillado y no solo con '':
print('Name:', info["name"])
print('Hide:', info["email"]["hide"])


si tenemos que imprimir una lista:

#print('List:', info['name']) ---> si los items de la lista son diccionarios, no ponemos la posicion del item dentro del [], si no
#cualquiera de las keys que tiene dentro el diccionario en esa posicion.

#python3 jason.py
#cd Desktop/Aitor/Coursera/Python/Using_Python_to_Acess_Web_Data/Week_6/code3
