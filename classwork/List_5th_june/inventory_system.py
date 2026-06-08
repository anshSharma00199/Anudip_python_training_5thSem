stock = [25, 5, 0, 12, 3, 18, 0, 30]

available = 0
new_list = []

print("Out of Stock Products:")
for i in range(len(stock)):
    if stock[i] == 0:
        print("Product", i + 1)

print("\nProducts Needing Restocking:")
for i in range(len(stock)):
    if stock[i] < 10:
        print("Product", i + 1, "Stock =", stock[i])

for i in stock:
    if i > 0:
        available += 1

for i in stock:
    if i >= 15:
        new_list.append(i)

print("\nAvailable Products:", available)
print("Products with Stock >= 15:", new_list)