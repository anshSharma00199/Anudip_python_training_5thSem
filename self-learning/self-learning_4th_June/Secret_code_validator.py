code = input("Enter a 6-digit secret code: ")

if len(code) == 6 and code.isdigit():
    first_sum = int(code[0]) + int(code[1]) + int(code[2])
    last_sum = int(code[3]) + int(code[4]) + int(code[5])

    if first_sum == last_sum:
        print("Valid Code")
    else:
        print("Invalid Code")
else:
    print("Invalid Code")