#cd Desktop/Aitor/Coursera/Python/Using_Python_to_Acess_Web_Data/Week_2
#python3 Extract_data.py
#import re
#x = 'My 2 favourite numbers are 19 and 42'
#y = re.findall('[0-9]+',x)
#print(y)

#import re
#fhand = open('mbox-short.txt')
#for line in fhand:
#    if re.search('^From ',line):
#        print(line)

#import re
#fhand = open('regex_sum_101228.txt')
#add = 0
#count = 0
#for line in fhand:
#    nums = re.findall('[0-9]+', line)
#    for num in nums:
#        inum = int(num)
#        add = add + inum
#        count = count + 1
#print('There are',count,'values','that add up to',add)

import re
print(sum(int[for values in re.findall('[0-9]+', open('regex_sum_101228.txt').read())]))
