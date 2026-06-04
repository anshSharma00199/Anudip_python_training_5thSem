num = input("Enter a number: ")

if len(num) % 2 == 0:
    mid = len(num) // 2

    left = num[:mid]
    right = num[mid:]

    if left == right:
        print("Mirror Number")
    else:
        print("Not a Mirror Number")
else:
    print("Not a Mirror Number")