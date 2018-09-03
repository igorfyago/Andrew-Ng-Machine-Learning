fname = input('Enter file:')
if len(fname) < 1: fname = 'clown.txt'
fhandle = open(fname)
counts = dict()
for line in fhandle:
    line = line.rstrip()
    words = line.split()
    for word in words:
        counts[word]= counts.get(word,0) + 1
print(counts)

lst = list()
for keys,values in counts.items():
    newtup = values,keys
    lst.append(newtup)
    lst = sorted(lst, reverse=True)
for values,keys in lst[:10]:
    print(keys,values)

#print(sorted([(values,keys) for keys,values in counts.items()], reverse=True))

#cd Desktop/Aitor/Coursera/Python/Python_Data_Structures/Week_6
#python3 tupples_v2.py
