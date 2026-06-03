a=float(input("enter First side: "))
b=float(input("enter Second side: "))
c=float(input("enter Third side: "))
if(a+b>c) and (a+c>b) and (b+c>a):
    if a==b and b==c and c==a:
        print("The given triangle is Equilateral triangle.")
    elif a==b or b==c or a==c:
        print("The given triangle is Isosceles triangle.")
    else:
        print("The given triangle is Equilateral triangle.")
else:
    print("The three sides cannot form a triangle.")