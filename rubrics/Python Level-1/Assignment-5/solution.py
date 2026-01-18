# Assignment 5: Inputs and Type Casting

# 1. Functions used so far
# print(), input(), type(), int(), float(), str()

# 2. Basic Input & String Formatting
# Method 1 (Direct prompt inside input - Shortcut 1)
first_name = input("Type your first name: ")
last_name  = input("Type your last name: ")

# Printing the welcome message
print("Welcome to Python Programing,", first_name, last_name + "!")

# 3. What does float(input()) do?
# float(input()) takes the user's text input and immediately converts it into 
# a decimal number (float). We need to use it whenever we expect the user 
# to type a number that might have decimals, like a price ($1.99) or a weight (15.5 kg).

# 4. Difference between int(input()) and float(input())
# int(input()) is for whole numbers (integers like 10, 5, -2).
# float(input()) is for decimal numbers (floats like 3.14, 0.5, 99.9).

# Example Code:
age   = int(input("Enter your age (whole number): ")) 
price = float(input("Enter price (decimal number): "))
print("Age:", age, "| Price:", price)

# 5. Two shortcut techniques for the input() function
# Shortcut 1: Writing the prompt message inside the input() function itself.
# Example:
hobby = input("What is your hobby? ")

# Shortcut 2: Wrapping the input() function inside a conversion function (int or float).
# Example:
score = int(input("Enter your score: "))

# Detailed Summary of Shortcuts:
# Instead of:
#   print("Enter name")
#   name = input()
# We do (Shortcut 1):
#   name = input("Enter name: ")

# Instead of:
#   num = input("Enter number: ")
#   num = int(num)
# We do (Shortcut 2):
#   num = int(input("Enter number: "))
