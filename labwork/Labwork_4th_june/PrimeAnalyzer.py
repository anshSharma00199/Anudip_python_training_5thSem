#Prime Number Analyzer
'Accept a number from the user and determine whether it is a prime number or not'

num=int(input("Enter the Number: "))
factors=[]
for i in range(1,num+1):
    if num%i==0:
        factors.append(i)
 
if len(factors)==2:
    print(f"{num} is a Prime Number")
else:
    print("Factors:",*factors)
    print(f"{num} is not a Prime numbers")