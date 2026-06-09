name = "Rahul Sharma"

print("Original Name:", name)

# Generate username
username = name.replace(" ", "")
username = username.lower()
username = username + "2026"

print("Generated Username:", username)

# Username length
length = len(username)
print("Username Length:", length)

# Keep first 12 characters if length exceeds 12
if len(username) > 12:
    short_username = username[:12]
else:
    short_username = username

# Count vowels and consonants
vowels = 0
consonants = 0

for ch in username:
    if ch.isalpha():
        if ch in "aeiou":
            vowels += 1
        else:
            consonants += 1

print("Vowels:", vowels)
print("Consonants:", consonants)

print("Status: Username Generated Successfully")