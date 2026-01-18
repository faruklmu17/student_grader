# Assignment 2: Python Syntax, Concatenation, and Debugging

# 1. What is syntax?
# Syntax refers to the specific set of rules that defines how a Python program 
# must be written. If you break these rules, the computer won't understand 
# your instructions.

# 2. What is concatenation?
# Concatenation is the process of joining two or more strings together 
# using the plus (+) operator.
greeting = "Hello" + " " + "World"
print("Concatenation Example:", greeting)

# 3. When are we NOT allowed to use plus (+)?
# We cannot use the plus operator to join a string and a number directly.
# Python doesn't know if it should do math or join text, so it throws a TypeError.
# Example of what NOT to do: print("My age is " + 25)

# 4. What is the difference between a = 3 and b = "3"?
# a = 3   -> This is an Integer (a whole number). You can do math with it.
# b = "3" -> This is a String (text). It is treated like a character, not a value for math.

# 5. Debugging Concepts
# - Bug: An error or flaw in a program that causes it to behave unexpectedly.
# - Debugging: The process of finding and fixing those bugs.
# - Common Error Messages: SyntaxError, NameError, TypeError, IndexError.

# 6. When do we get a "SyntaxError"?
# This happens when you break the rules of the language, such as forgetting 
# a quote mark, a parenthesis, or misspelling a keyword like 'prnt' instead of 'print'.

# 7. When do we get a "NameError"?
# This happens when you try to use a variable name that hasn't been created yet.
# For example, trying to print(x) before you ever said x = 10.

# 8. Fix the following line of code:
# Original: print("I am learning Python"+ 3+,"and working on"+"assignment #"+2+".")
# Rule: Only change the + and/or comma.
# Fix: We use commas to safely mix strings and numbers in a print statement.

print("I am learning Python", 3, ", and working on", "assignment #", 2, ".")

# Note: Using commas automatically adds a space between the items. 
# This is the easiest way for beginners to print different types of data together!
