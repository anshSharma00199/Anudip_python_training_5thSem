'''A teacher is recording a student attendence the strength of class is 30, everytime is need to insert student is present or absent, 
   so count the total number of student present as well as absent'''

present = 0
absent = 0
for i in range(1,31,1):
    print(f"Student {i}:")
    Student=input(f"Attendence:")
    print(" ")
    if(Student=="p"):
        present+=1
    else:
        absent+=1

print("No. of Present Students:", present)
print("No. of Absent Student: ", absent)

