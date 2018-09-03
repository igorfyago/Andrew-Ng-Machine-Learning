fname = input('Enter file:')
if len(fname) < 1 : fname = 'clown.txt'
fhandle = open(fname)
counts = dict()
for line in fhandle:
    line = line.rstrip()
    words = line.split()
    print(words)
    for word in words:
        counts[word] = counts.get(word,0) + 1
    print(counts)
#ahora queremos hacer una lista con tupples dentro pero con valores primero y palabras despues:
lst = list()
for keys,values in counts.items():
    newtup = (values,keys)
    lst.append(newtup)
    lst = sorted(lst, reverse=True)
print(lst)
for values, keys in lst[:10]:
print(keys,values)

#y el metodo abreviado para escribir de la 13 a la 16 y de la 16  a la 20 en una sola linea es:
#print(sorted([(keys,values) for values,keys in counts.items()], reverse=True))




#cd Desktop/Aitor/Coursera/Python/Python_Data_Structures/Week_6
#python3 tupples.py
