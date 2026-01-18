# Assignment 8: Nested Functions and Output Analysis

# 1. str(2.0)
print("The output of print(str(2.0)) is '2.0'.")
print("Explanation: It converts the float 2.0 into the text/string '2.0'.")

# 2. type(float("2"))
print("\nThe output of print(type(float('2'))) is <class 'float'>.")
print("Explanation: First, '2' is converted to a decimal 2.0, then type() identifies it as a float.")

# 3. int(2.5)
print("\nThe output of print(int(2.5)) is 2.")
print("Explanation: The int() function truncates (chops off) the decimal part, it does not round.")

# 4. input() result
print("\nThe output of print(input('What’s your name: ')) depends on what you type.")
print("Explanation: The input() function captures what the user types, and print() displays it.")

# 5. type(round(2.34, 1))
print("\nThe output of print(type(round(2.34,1))) is <class 'float'>.")
print("Explanation: Rounding 2.34 to one decimal result in 2.3, which is still a float.")

# 6. type of input
print("\nThe output of print(type(input('How old are you: '))) is ALWAYS <class 'str'>.")
print("Explanation: In Python, input() always returns text (a string), regardless of what characters were typed.")

# 7. len(str(234.0))
print("\nThe output of print(len(str(234.0))) is 5.")
print("Explanation: str(234.0) becomes '234.0'. Counting everything including the dot and zero gives 5.")

# 8. int(input())
print("\nThe output of print(int(input('What’s your favourite number?'))) is the whole number version of your input.")
print("Explanation: It takes the user's string input and converts it into a real integer number before printing.")
