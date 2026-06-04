correct_pin="1234"
while True:
    pin=input("enter your 4-digit pin :")
    if(len(pin)!=4):
        print("Pin should be 4-digit ")
    elif(pin==correct_pin):
        print("Access Granted")
        break
    else:
        print("Incorrect Pin. Try Again...")