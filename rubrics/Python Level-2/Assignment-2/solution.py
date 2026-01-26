# Assignment-2 Python Level-2 Solution

# 1. Explain (using code) the difference between the two keywords: int and float.
# int: whole numbers without decimals (e.g., 5, -10)
# float: numbers with decimals (e.g., 5.5, -10.2)
num_int = 10
num_float = 10.5
print(f"Int example: {num_int}")
print(f"Float example: {num_float}")

# 2. How can we check if a number is float or int?
# We can use the type() function.
print(f"Type of num_int: {type(num_int)}")
print(f"Type of num_float: {type(num_float)}")

# 3. Using code, check and print that if a number is int or float
number = 7.5
if type(number) == int:
    print("The number is an int")
elif type(number) == float:
    print("The number is a float")

# 4. What is the difference between the AND and OR operator? Write an example code to show the difference
# AND: Returns True only if BOTH conditions are True.
# OR: Returns True if AT LEAST ONE condition is True.

print("AND example (True and False):", True and False) # False
print("OR example (True or False):", True or False)   # True

# Scenario Part-1 & Part-2
money = 10
mars = 2.25
kitkat = 5.50

# Part-1: if Mars is less than Kitkat and Mars costs less than $2.50, print that I will buy the Mars.
if mars < kitkat and mars < 2.50:
    print("I will buy the Mars")
    
    # Show how much you have left after buying the Mars. Save the left amount in a variable.
    left_amount = money - mars
    print(f"Money left: ${left_amount}")
    
    # Part-2: Check if the left amount is at least $5.50 or more than $5.50
    if left_amount >= 5.50:
        print("you can afford to buy a Kitkat too!")
