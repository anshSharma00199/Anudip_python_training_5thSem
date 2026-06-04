#Porblem Statement : Attendence Counter
attendence_count=0
class_strength=30
Student_present= True
while(attendence_count<class_strength):
    if(Student_present):
        print("Student Entered")
        attendence_count+=1
        print("Attendence count:",attendence_count)
        print(" ")
    else:
        break
