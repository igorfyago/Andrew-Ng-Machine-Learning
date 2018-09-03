#10.2 Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day
#for each of the messages. You can pull the hour out from the 'From ' line by finding the time and then splitting
#the string a second time using a colon.
#Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.

fname = input('Enter file:')
if len(fname) < 1: fname = 'mbox-short.txt'
fhandle = open(fname)
counts = dict()
for line in fhandle:
    if not line.startswith('From '):
        continue
    line = line.rstrip()
    words = line.split()
    sspl = words[5].split(':')
    hour = sspl[0]
    counts[hour] = counts.get(hour,0) + 1
print(counts.items())
#print(counts)
#lst = list()
#for keys,values in counts.items():
    #newtup = values,keys
    #lst.append(newtup)
    #lst.sort()
#print(lst)
#for keys,values in lst[:]:
    #print(keys,values)

#Como nos piden que ordenemos por keys y no por values, no necesitamos darle la vuelta a la lista y solo seria:
#lst = sorted(counts.items())
#for keys,values in lst[:]:
#    print(keys,values)

#cd Desktop/Aitor/Coursera/Python/Python_Data_Structures/Week_6
#python3 Assignment_10_2.py
