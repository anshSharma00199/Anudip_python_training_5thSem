products = [
    (101, "Pass"),
    (102, "Fail"),
    (103, "Pass"),
    (104, "Fail"),
    (105, "Pass")
]

passed = 0
failed = 0

print("Failed Product IDs:")

for pid, status in products:
    if status == "Fail":
        print(pid)
        failed += 1
    else:
        passed += 1

print("Passed Products:", passed)
print("Failed Products:", failed)

percentage = (passed / len(products)) * 100

print("Pass Percentage:", percentage)

fail_count = 0

for pid, status in products:
    if status == "Fail":
        fail_count += 1

    if fail_count == 3:
        print("3 Failures Found")
        break