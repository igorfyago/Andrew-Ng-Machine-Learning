#cd ~/Desktop/Aitor/Coursera/Python/Python_Data_Structures/Week_1
fruit = 'banana'
pos = fruit.find('na')
print(pos)

greet = 'Hello Bob'
nstr = greet.replace('o','x')
print(nstr)

data = 'From stephen.marquard@uct.az.ca Sat Jan 5'
atpos = data.find('@')
print(atpos)
sppos = data.find(' ',atpos)
print(sppos)
host = data [atpos+1 : sppos]
print(host)

for letter in 'banana':
    print(letter)
