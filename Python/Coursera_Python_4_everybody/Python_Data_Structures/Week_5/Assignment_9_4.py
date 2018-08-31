#9.4 Write a program to read through the mbox-short.txt and figure out who has the sent the greatest number of mail messages. The program looks for
# 'From ' lines and takes the second word of those lines as the person who sent the mail. The program creates a Python dictionary
#that maps the sender's mail address to a count of the number of times they appear in the file. After the dictionary is
#produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.
fname = input('Enter file:')
if len(fname) < 1 : fname = 'clown.txt'
handle = open(fname)
list = dict()

for line in handle:
    if not line.startswith('From '):
        continue
#I make a list
    line = line.rstrip()
    wds = line.split()
    #print(wds[1])
#I get the second item of the list and assign to a constant
    sender = wds[1]
#I add that constant to the dictionary "list"
    list[sender] = list.get(sender,0) + 1
print(list)
#I make a for loop to get maximum key and values
    #bigvalue = None
    #bigkey = None
    #for keys,values in list.items():
        #if bigvalue is None or values > bigvalue:
        #    bigvalue = values
        #    bigkey = keys
#print(bigkey,bigvalue)



#cd Desktop/Aitor/Coursera/Python/Python_Data_Structures/Week_5
#python3 Assignment_9_4.py
