#Open the file romeo.txt and read it line by line. For each line, split the line into a list of words using the split() method.
#The program should build a list of words. For each word on each line check to see if the
#word is already in the list and if not append it to the list. When the program completes, sort and print
#the resulting words in alphabetical order.You can download the sample data at

fname = input("Enter file name: ")
if len(fname) < 1 : fname = 'romeo.txt'
fh = open(fname)
lst = list()
for line in fh:
    line = line.rstrip()
    line = line.split()
    for i in range(len(line)):
        word = line[i]
        if not word in lst:
            lst.append(word)
    #for i in line:
        #if not i in lst:
            #lst.append(i)
lst.sort()
print(lst)

#cd Desktop/Aitor/Coursera/Python/Python_Data_Structures/Week_4
#python3 Assignment_8_4.py
