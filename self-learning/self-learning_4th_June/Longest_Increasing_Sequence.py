n = int(input("Enter number of elements: "))

max_len = 1
current_len = 1

prev = int(input("Enter number: "))

for i in range(1, n):
    num = int(input("Enter number: "))

    if num > prev:
        current_len += 1
    else:
        if current_len > max_len:
            max_len = current_len
        current_len = 1

    prev = num

if current_len > max_len:
    max_len = current_len

print("Longest Sequence Length =", max_len)