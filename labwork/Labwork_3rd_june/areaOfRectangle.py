l=float(input("enter the rectangle: "))
if(l<=0):
    print("The length cannot be negative... try again")
    exit()
b=float(input("Enter the breadth: "))
if(b<=0):
    print("The breadth cannot be negative... try again")
    exit()
else:
    perimeter=2*(l+b)
    area=l*b
    print(f"The Perimeter of the reactangle having length {l} and breadth {b} : {perimeter}")
    print(f"The Area of the reactangle having length {l} and breadth {b} : {area}")

