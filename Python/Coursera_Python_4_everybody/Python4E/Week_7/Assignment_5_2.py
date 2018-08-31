#5.2 Write a program that repeatedly prompts a user for integer numbers until the user enters 'done'. Once 'done' is entered,
#print out the largest and smallest of the numbers. If the user enters anything other than a valid number catch it with a try/except
#and put out an appropriate message and ignore the number.
#Enter 7, 2, bob, 10, and 4 and match the output below.

largest = None
smallest = None
while True:
    num = input('Enter a number:')
#Clavar el error con try/except
#Si pone "done" salimos del loop
    if num == 'done' :
        break
    try:
        num = int(num)
    except:
        print('Invalid input')
        continue
#Clavar el mayor y el menor
    if largest is None:
            largest = num
    elif num > largest:
            largest = num
    if smallest is None:
            smallest = num
    elif num < smallest:
            smallest = num
#Y los prints
print('Maximum is', largest)
print('Minimum is', smallest)
