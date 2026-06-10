# Function to count different types of reviews
def count_sentiments(reviews):
    excellent = 0
    good = 0
    average = 0
    poor = 0

    # Count each sentiment
    for i in reviews:
        if "excellent" in i:
            excellent += 1
        elif "good" in i:
            good += 1
        elif "average" in i:
            average += 1
        elif "poor" in i:
            poor += 1

    return excellent, good, average, poor


# Function to find the most common word
def most_common_word(reviews):
    words = []

    # Store all words in a list
    for i in reviews:
        x = i.split()
        for j in x:
            words.append(j)

    max_count = 0
    common = ""

    # Find the word with maximum frequency
    for i in words:
        count = words.count(i)
        if count > max_count:
            max_count = count
            common = i

    return common


# Function to find the longest review
def longest_review(reviews):
    longest = reviews[0]

    for i in reviews:
        if len(i) > len(longest):
            longest = i

    return longest


# Function to display reviews containing a keyword
def reviews_with_keyword(reviews, keyword):
    print("Reviews containing", keyword + ":")

    for i in reviews:
        if keyword in i:
            print(i)


