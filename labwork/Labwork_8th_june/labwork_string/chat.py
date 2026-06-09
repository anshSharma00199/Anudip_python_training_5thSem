message = "Python is awesome and Python is easy to learn"

print("Message:", message)

# Total characters
print("\nTotal Characters:", len(message))

# Split message into words
words = message.split()

# Total words
print("Total Words:", len(words))

# Longest and shortest word
longest = words[0]
shortest = words[0]

for word in words:
    if len(word) > len(longest):
        longest = word
    if len(word) < len(shortest):
        shortest = word

print("Longest Word:", longest)
print("Shortest Word:", shortest)

# Count Python occurrences
count = 0
for word in words:
    if word == "Python":
        count += 1

print("Occurrences of Python:", count)

# Words with more than 4 characters
long_words = []

for word in words:
    if len(word) > 4:
        long_words.append(word)

print("Words Longer Than 4 Characters:", long_words)

# Words starting with a vowel
print("Words Starting With a Vowel:")
for word in words:
    if word[0].lower() in "aeiou":
        print(word)

# Count vowels and consonants
vowels = 0
consonants = 0

for ch in message.lower():
    if ch.isalpha():
        if ch in "aeiou":
            vowels += 1
        else:
            consonants += 1

print("Vowels:", vowels)
print("Consonants:", consonants)