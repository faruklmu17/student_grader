# Assignment 1: Introduction to Python
# This script covers the basics of printing, variables, comments, and syntax.

# 1. Printing key terms
# We use the print() function to display text on the screen.
print("Variable")
print("String")
print("Syntax")

# 2. Printing definitions
# A Variable is a container used to store data values.
print("Variable: A container for storing data values.")

# A String is a sequence of characters (text) wrapped in quotes.
print("String: A sequence of characters enclosed in 'single' or \"double\" quotes.")

# Syntax refers to the set of rules that defines how a Python program is written and interpreted.
print("Syntax: The set of rules that define the structure of the language.")

# 3. Single-line comments
# We use the hash symbol (#) to write a comment that only takes up one line.
# This line is a comment and will not be executed by Python!

# 4. Printing a specific sentence
print("I am learning Python.")

# 5. Creating and printing four variables
# Here we create two variables for numbers and two for strings.
age = 25              # A number (integer)
price = 19.99         # A number (float)
name = "Alice"        # A string
course = "Python 101" # A string

# Printing the variables to see their current values
print("Initial Values:")
print(age)
print(price)
print(name)
print(course)

# 6. Assigning new values (Reassignment)
# When we assign a new value to a variable that already exists, 
# Python replaces the old value with the new one. This is called reassignment.
age = 30
price = 24.50
name = "Bob"
course = "Advanced Python"

print("\nUpdated Values:")
print(age)
print(price)
print(name)
print(course)

# Detailed Explanation:
# When we wrote 'age = 30', Python looked for the existing 'age' variable
# and updated its memory to store '30' instead of '25'. The previous value 
# is gone forever unless we stored it somewhere else first.

# 7. Rules for creating variables
# - Variable names must start with a letter or an underscore (_).
# - Variable names cannot start with a number.
# - Variable names can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ ).
# - Variable names are case-sensitive (age, Age, and AGE are three different variables).
# - Variable names cannot be Python keywords (like 'print', 'if', 'while', etc.).

# 8. The Assignment Operator
# The '=' sign is known as the assignment operator in Python.
# It is used to assign the value on the right-hand side to the variable on the left-hand side.

# Example:
score = 100 
# In the example above, '=' takes the value 100 and assigns it to the variable named 'score'.
