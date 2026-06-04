correct_password= "admin123" 
while True:
    pin=input("Enter password:")
    if(pin==correct_password):
        print("Login Successful")
        break
    else:
        print("Invalid Password")