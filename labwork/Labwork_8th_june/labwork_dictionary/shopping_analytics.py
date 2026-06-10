sales = {
    "Laptop": 15,
    "Mouse": 45,
    "Keyboard": 32,
    "Monitor": 12,
    "Headphones": 28,
    "Printer": 8,
    "Webcam": 20,
    "Speaker": 18,
    "Tablet": 10,
    "Router": 25
}

# 1. Products sold more than 20 times
print("Products Sold More Than 20 Times:")
for product, count in sales.items():
    if count > 20:
        print(product)

# 2. Best-selling product
best = max(sales, key=sales.get)
print("\nBest Selling Product:", best, "(", sales[best], ")", sep="")

# 3. Least-selling product
least = min(sales, key=sales.get)
print("Least Selling Product:", least, "(", sales[least], ")", sep="")

# 4. Total products sold
total = sum(sales.values())
print("Total Units Sold:", total)

# 5. Products requiring promotion
promotion = []
for product, count in sales.items():
    if count < 15:
        promotion.append(product)

print("Products Requiring Promotion:", promotion)

# 6. Count products having sales between 10 and 30
count = 0
for value in sales.values():
    if 10 <= value <= 30:
        count += 1

print("Products Having Sales Between 10 and 30:", count)