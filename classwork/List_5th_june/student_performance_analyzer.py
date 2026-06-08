marks=[78,45,92,35,88,40,99,56]
print("Passed Students:")
count=0
for i in marks:
    if(i>=40):
        print(i)
    else:
        count+=1
print("Failed students:",count)
print("Highest marks: ",max(marks))
print("Lowest marks: ",min(marks))

new_list=[]
for i in marks:
    if i > 75:
        new_list.append(i)
print("New List having marks above 75:",new_list)