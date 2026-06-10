text = "AAABBBCCCDDDAAA"

freq = {}

for i in text:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1

print("Original Text:", text)

print("Character Frequencies:")
for i in freq:
    print(i, "->", freq[i])

unique = list(freq.keys())
print("Unique Characters:", unique)

# Most Frequent Character
max_char = ""
max_count = 0

for i in freq:
    if freq[i] > max_count:
        max_count = freq[i]
        max_char = i

print("Most Frequent Character:", max_char)

# Compression
compressed = ""
count = 1

for i in range(len(text)-1):
    if text[i] == text[i+1]:
        count += 1
    else:
        compressed += text[i] + str(count)
        count = 1

compressed += text[-1] + str(count)

print("Compressed Output:", compressed)

original_len = len(text)
compressed_len = len(compressed)

ratio = (compressed_len / original_len) * 100

print("Original Length:", original_len)
print("Compressed Length:", compressed_len)
print("Compression Ratio:", round(ratio, 2), "%")