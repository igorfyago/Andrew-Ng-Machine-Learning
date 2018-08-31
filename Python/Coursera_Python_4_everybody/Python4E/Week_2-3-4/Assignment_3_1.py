hrs = input("Enter Hours:")
try:
    h = float(hrs)
except:
    h = -1
if h > 0 :
    rte = input("Enter rate per hour")
else:
    print("Its not a number")

try:
    r = float(rte)
except:
    r = -1
if r > 0 :
    if h <= 40 :
        print(h*r)
    elif h > 40 :
        print(40*r+(h-40)*1.5*r)
else:
    print("Its not a number")
