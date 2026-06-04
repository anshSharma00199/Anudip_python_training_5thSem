high_count = 0
low_count = 0
total_amount = 0

while True:
    amount = float(input("Enter transaction amount (-1 to stop): "))

    if amount == -1:
        break

    total_amount += amount

    if amount > 50000:
        high_count += 1

    if amount < 1000:
        low_count += 1

print("Transactions above ₹50,000 =", high_count)
print("Transactions below ₹1,000 =", low_count)
print("Total Transaction Amount = ₹", total_amount)