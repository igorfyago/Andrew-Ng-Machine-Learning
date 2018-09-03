def computepay(h,r):
    fh = float(h)
    fr = float(r)
    if fh <= 40 :
        return fh*fr
    else:
        return fh*fr+0.5*(fh-40)*fr


h = input("Enter Hours:")
r = input("Enter rate")
p = computepay(h,r)
print(p)
