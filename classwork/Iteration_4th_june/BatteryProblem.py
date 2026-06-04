CurrentBattery= 20
electricity_status= True
while CurrentBattery<100:
    if(electricity_status):
        print("Now Battery Level: ", CurrentBattery, "%")
        CurrentBattery+=10
    else:
        break

print("Full Charge")