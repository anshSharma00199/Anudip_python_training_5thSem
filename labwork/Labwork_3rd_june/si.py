#program to find simple interest
p=int(input("enter the principle:"))
if p<0:
    print("Principle can't be negative")
    exit()
r=int(input("enter the rate:"))
if r<0:
    print("Rate of Interest can't be negative")
    exit()
t=int(input("enter the time:"))
if t<0:
    print("Any value can't be negative")
    exit()
else:
    si=(p*r*t)/100
    print("The simple interest is : ", si)

#write a program to check the sides are making triangle or not in self learning

