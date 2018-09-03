#cd ~/Desktop/Aitor/Coursera/Python/Python_Data_Structures/Week_1
fruit = 'banana'
letter = fruit [4]
print(fruit[0])
x = 3
w = fruit[4-x]
print(w)

zot = 'abc'
print(zot[2])

fruit = 'banana'
index = 0
while index < len(fruit) :
    letter = fruit[index]
    print(index,letter)
    index = index +1

fruit = 'banana'
for a in fruit :
    print(a)

word = 'banana'
count = 0
for letter in word :
    if letter == 'a':
        count = count + 1
print(count)

x = 'Monty Python'
print(x[0:4])
print(x[5:])
print(x[:])
