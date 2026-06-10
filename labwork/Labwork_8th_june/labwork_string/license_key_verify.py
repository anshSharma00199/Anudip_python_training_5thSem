key = "ABCD-EFGH-IJKL-MNOP"

groups = key.split("-")

valid = True

if len(groups) != 4:
    valid = False

for i in groups:
    if len(i) != 4:
        valid = False

merged = key.replace("-", "")

letters = len(merged)

vowels = 0
for i in merged:
    if i in "AEIOUaeiou":
        vowels += 1

print("License Key:", key)
print("Groups:", groups)
print("Number of Groups:", len(groups))
print("Total Letters:", letters)
print("Total Vowels:", vowels)
print("Merged Key:", merged)

if valid:
    print("License Key Status: Valid")
else:
    print("License Key Status: Invalid")