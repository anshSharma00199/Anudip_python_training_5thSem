emp_id = "EMP2026ANUJ458"

# 1. Count uppercase letters
upper = 0
for i in emp_id:
    if i.isupper():
        upper += 1

# 2. Count digits
digit_count = 0
for i in emp_id:
    if i.isdigit():
        digit_count += 1

# 3. Extract joining year
year = emp_id[3:7]

# 4. Extract employee name
name = emp_id[7:-3]

# 5. Validate ID
valid = True

if not emp_id.startswith("EMP"):
    valid = False

if not year.isdigit() or len(year) != 4:
    valid = False

if not emp_id[-3:].isdigit():
    valid = False

# 6. Create digit list
digit_list = []
for i in emp_id:
    if i.isdigit():
        digit_list.append(int(i))

# 7. Sum of digits
digit_sum = sum(digit_list)

# 8. Display results
print("Employee ID:", emp_id)
print("Uppercase Letters:", upper)
print("Digits:", digit_count)
print("Joining Year:", year)
print("Employee Name:", name)
print("Digit List:", digit_list)
print("Sum of Digits:", digit_sum)

if valid:
    print("ID Status: Valid")
else:
    print("ID Status: Invalid")