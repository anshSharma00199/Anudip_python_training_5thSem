a=float(input("enter First side: "))
b=float(input("enter Second side: "))
c=float(input("enter Third side: "))
if(a+b>c) and (a+c>b) and (b+c>a):
    print("The three sides can form a triangle.")
else:
    print("The three sides cannot form a triangle.")