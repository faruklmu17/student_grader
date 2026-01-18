# Assignment 10: Built-in Functions Review

# 1. What is a built-in function?
# Built-in functions are functions that are built into the Python language 
# and are always available for use without needing to import any extra modules.

# 2. Examples of Built-in Functions:

# print() - Outputs data to the screen
print("Hello, this is a print statement!")

# input() - Receives data from the user
name = input("Enter your name: ")

# int() - Converts a value to an integer
num_str = "10"
num_int = int(num_str)
print("Converted string to integer:", num_int)

# str() - Converts a value to a string
age = 25
age_str = str(age)
print("Converted integer to string: " + age_str)

# float() - Converts a value to a decimal number
price_str = "19.99"
price_float = float(price_str)
print("Converted string to float:", price_float)

# type() - Returns the data type of an object
x = 100
print("The type of x is:", type(x))

# len() - Returns the length (number of items) of an object
fruits = ["apple", "banana", "cherry"]
print("The number of items in the list is:", len(fruits))

# list() - Converts an iterable into a list
word = "Python"
chars = list(word)
print("String converted to list of characters:", chars)

# round() - Rounds a number to a specific precision
pi = 3.14159
print("Rounded pi to 2 decimal places:", round(pi, 2))
