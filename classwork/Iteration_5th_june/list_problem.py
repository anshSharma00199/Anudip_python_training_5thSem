#wap to create a list of twenty numbers given by user. Ask user to input any other number. 
#Remove all duplicate of enter number by user from list
list1=[]
print("----Enter 20 Numbers----")
for i in range(1,21):
    num=int(input(f"Enter {i} numbers: "))
    list1.append(num)
print("\nOriginal List:")
print(list1)

n=int(input("Enter the number you want to remove: "))
count = 0
new_list = []

for item in list1:
    if item == n:
        count += 1
        if count == 1:  
            new_list.append(item)
    else:
        new_list.append(item)

print("Updated List:", new_list)