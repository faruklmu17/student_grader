# Assignment 4: Comparison Operators and Conditionals

# 1. Three Comparison Operators Examples
# == (Equal to)
# >  (Greater than)
# <  (Less than)
print(10 == 10) # True
print(15 > 5)   # True
print(2 < 8)    # True

# 2. String Comparison
# str1 = "Hello", str2 = "hello"
# Expression: str1 == str2
# Output: False (Python is case-sensitive)

# 3. Numeric Comparison (Int vs Float)
# x = 5, y = 5.0
# Expression: x == y
# Output: a) True (Python compares the value, and 5 is equal to 5.0)

# 4. Two choices Python provides when comparing numbers
# Python provides: True and False (Booleans)

# 5. Difference between = and ==
# =  is the "Assignment Operator". It is used to give a value to a variable.
# == is the "Comparison Operator". It is used to check if two values are equal.

# 6. Doritos and Lays Task
doritos = 3.10
lays = 3.20

# First check: If doritos is less than lays
if doritos < lays:
    print("doritos is less expensive than lays!")

# Changing the price of doritos (Reassignment)
doritos = 3.50

# Using elif to check if doritos is more than lays
if doritos > lays:
    print("doritos is more expensive than lays")

# Optional: To match the "if...elif...elif" structure exactly as requested in a single logical flow:
# Note to students: Usually we use one if block, but here we show the logic step-by-step.

doritos = 3.20
if doritos < lays:
    print("doritos is less expensive than lays!")
elif doritos > lays:
    print("doritos is more expensive than lays")
elif doritos == lays:
    print("I can buy any of them!")
