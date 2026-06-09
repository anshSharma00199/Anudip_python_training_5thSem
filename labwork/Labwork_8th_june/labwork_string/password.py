password = "Python@2026!"

upper = 0
lower = 0
digits = 0
special = 0

digit_list = []
special_list = []

for ch in password:
    if ch.isupper():
        upper += 1
    elif ch.islower():
        lower += 1
    elif ch.isdigit():
        digits += 1
        digit_list.append(ch)
    else:
        special += 1
        special_list.append(ch)

print("Password:", password)
print("Uppercase Letters:", upper)
print("Lowercase Letters:", lower)
print("Digits:", digits)
print("Special Characters:", special)
print("Digits Found:", digit_list)
print("Special Characters Found:", special_list)

# Check password strength
if (len(password) >= 8 and upper >= 1 and lower >= 1
        and digits >= 1 and special >= 1):
    print("Password Strength: Strong")
elif len(password) >= 6 and (upper + lower) > 0 and digits > 0:
    print("Password Strength: Medium")
else:
    print("Password Strength: Weak")
    