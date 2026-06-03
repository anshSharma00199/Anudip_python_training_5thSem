l=int(input("enter the rectangle: "))
if(l<=0):
    print("The length cannot be negative... try again")
    exit()
b=int(input("Enter the breadth: "))
if(b<=0):
    print("The breadth cannot be negative... try again")
    exit()
else:
    area=l*b
    print(f"The Area of the reactangle having length {l} and breadth {b} : {area}")

