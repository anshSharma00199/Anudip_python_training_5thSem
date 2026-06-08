#wap to create a list of twenty numbers given by user. Ask user to input any other number. 
#Remove all duplicate of enter number by user from list
numbers=[]
print("----Enter 20 Numbers----")
for x in range(1,21):
    num=int(input(f"Enter {x} numbers: "))
    numbers.append(num)
print("\nOriginal List:")
print(numbers)

element=int(input("Enter the number you want to remove: "))
#finding the frequency of given number
frequency= numbers.count(element)
if frequency ==0:
    print("element not found.")
elif frequency==1:
    print("No duplicates found")
else:

    #reversing the list
    numbers.reverse()
    for i in range (1, frequency):
        numbers.remove(element)
    #reevrse the element again
    numbers.reverse()
    print("After Removing Duplicates:")
    print(numbers)