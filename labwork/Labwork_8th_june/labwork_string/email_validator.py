email = "rahul.sharma2026@gmail.com"

print("Email:", email)

# 1. Username
username = email.split("@")[0]

# 2. Domain
domain = email.split("@")[1].split(".")[0]

# 3. Extension
extension = email.split(".")[-1]

print("Username:", username)
print("Domain:", domain)
print("Extension:", extension)

# 4. Count digits in username
digits = 0

for ch in username:
    if ch.isdigit():
        digits += 1

print("Digits Found:", digits)

# 5. Count special characters
special = 0

for ch in email:
    if not ch.isalnum():
        special += 1

print("Special Characters Found:", special)

# 6. Validate email
if email.count("@") == 1 and "." in email.split("@")[1]:
    print("Email Status: Valid")
else:
    print("Email Status: Invalid")