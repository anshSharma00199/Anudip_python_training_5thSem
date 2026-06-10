from movie_review import *

# Main Program

# List of movie reviews
reviews = [
    "excellent movie",
    "average story",
    "excellent acting",
    "poor direction",
    "excellent visuals",
    "poor screenplay",
    "good music",
    "excellent climax",
    "average performance",
    "good cinematography"
]

# Count sentiments
excellent, good, average, poor = count_sentiments(reviews)

# Display sentiment counts
print("Excellent Reviews:", excellent)
print("Good Reviews:", good)
print("Average Reviews:", average)
print("Poor Reviews:", poor)

# Display most common word
print("\nMost Common Word:", most_common_word(reviews))

# Display longest review
print("Longest Review:", longest_review(reviews))

print()

# Display reviews containing the keyword "excellent"
reviews_with_keyword(reviews, "excellent")
