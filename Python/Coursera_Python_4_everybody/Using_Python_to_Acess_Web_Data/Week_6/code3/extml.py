import xml.etree.ElementTree as ET

data = '''
<person>
  <name>Chuck</name>
  <phone type="intl">
     +1 734 303 4456
   </phone>
   <email hide="yes"/>
</person>'''


tree = ET.fromstring(data) #tree en este punto se convirte en un objeto, en un arbol
print('Name:', tree.find('name').text)#Accordarme de que el .find de un string normal nos da la posicion
# en este caso el .find es el name y "chuck", que cuelga de name. Si añadimos el .text es solo "chuck"
print('Attr:', tree.find('email').get('hide'))# el atributo no se consigue con .text si no con .get

#python3 extml.py
#cd Desktop/Aitor/Coursera/Python/Using_Python_to_Acess_Web_Data/Week_5/code3
