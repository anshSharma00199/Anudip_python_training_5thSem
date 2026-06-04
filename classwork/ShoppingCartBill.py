total=0
while True:
    Price=int(input("Enter Item Price: "))
    if(Price==0):
        break
    if(Price<0):
        print("Price can't be negative. Try Again")
        continue
    total=total + Price
print("Total bill Amount: Rs. ", total)