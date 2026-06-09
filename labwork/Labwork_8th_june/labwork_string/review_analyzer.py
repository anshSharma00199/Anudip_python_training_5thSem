review = "This product is excellent excellent excellent and very useful"

words = review.split()

# 1. Total words
print("Total Words:", len(words))

# 2. Word frequencies
frequency = {}

for word in words:
    if word in frequency:
        frequency[word] += 1
    else:
        frequency[word] = 1

print("\nWord Frequencies:")
for key, value in frequency.items():
    print(key, "->", value)

# 3. Most frequent word
max_word = ""
max_count = 0

for key, value in frequency.items():
    if value > max_count:
        max_count = value
        max_word = key

print("\nMost Frequent Word:", max_word)

# 4. Words appearing once
single = []

for key, value in frequency.items():
    if value == 1:
        single.append(key)

print("Words Appearing Once:", single)

# 5. Words having more than 5 characters
count = 0

for word in words:
    if len(word) > 5:
        count += 1

print("Words Longer Than 5 Characters:", count)

# 6. Words in reverse order
print("Words in Reverse Order:")
for word in words[::-1]:
    print(word)

# 7. Unique words
unique = []

for word in words:
    if word not in unique:
        unique.append(word)

print("Unique Words:", unique)