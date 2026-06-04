'Check whther the number given by the user is armstrong or not'
num=int(input("Enter the number:"))
order=len(str(num))
temp=num
total=0
while temp>0:
    d=temp%10
    total+=d**order
    temp//=10
if total==num:
    print("Armstrong number")
else:
    print("Not a armstrong")
