#program to covert time into corresponding hour, minute and second
second= int(input("enter the time in seconds: "))
if(second<0):
    exit("Time cant be negative.... Exited")
print("...............................................")
hour=0
minute=0

#coverting number of second into hours
if(second>=3600):
    hour=second //3600
    second = second % 3600

#converting into minute
if(second>=60):
    minute=second // 60
    second= second % 60

print(f"The time is {hour} hours {minute} minutes {second} seconds")