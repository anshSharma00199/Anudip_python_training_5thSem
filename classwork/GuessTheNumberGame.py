secret_number= 7
while True:
    num=int(input("Guess the number:"))
    if(num==secret_number):
        print("Congratulations! you choose the correct number.")
        break
    else:
        print("Wrong guess, Try Again.")
