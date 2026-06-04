num = int(input("Enter a number: "))

temp = num
prev = temp % 10
temp //= 10

is_consecutive = True

while temp > 0:
    digit = temp % 10

    if prev - digit != 1:
        is_consecutive = False
        break

    prev = digit
    temp //= 10

if is_consecutive:
    print("Consecutive Number")
else:
    print("Not a Consecutive Number")