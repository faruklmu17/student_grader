# Assignment 6: Logical Operators

# 1. Three logical operators
# and
# or
# not

# 2. Difference between AND and OR
# The AND operator returns True only if BOTH conditions are True.
# The OR operator returns True if AT LEAST ONE condition is True.
# You use AND when you want to be strict (e.g., checking if a score is between 90 AND 100).
# You use OR when you want to be flexible (e.g., checking if it's Saturday OR Sunday).

# 3. Variable check with logical operator
num = 7
if num < 10 and num < 20:
    print("You typed a number that is both less than 20 and 10!")

# 4. Grade validation using logical operators
# We use 'and' to check if a number is inside a specific range (90 to 100)
# We use 'or' to check if a number is outside that range (less than 90 OR more than 100)

score = 95 # Example score

if score >= 90 and score <= 100:
    print("You got an A grade!")
elif score < 90 or score > 100:
    print("You typed an invalid number!")

# Example with an invalid number:
score = 105
if score >= 90 and score <= 100:
    print("You got an A grade!")
elif score < 90 or score > 100:
    print("You typed an invalid number!")
