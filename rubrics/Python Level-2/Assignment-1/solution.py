# Assignment -1 Python Level-2 Solution

# 1. Print the following word list (from 1 to 10 and using only one print() statement)
print("""1. Programming Language
2. Pseudocode
3. Binary Number
4. Syntax
5. Variable
6. Data Type
7. Whole Number
8. Integer Number
9. Logical operator
10. Debugging""")

# 2. After printing the list, print: Type a word to see the definition-
# 3. Save the typed word in a variable.
word = input("Type a word to see the definition- ")

# 4. Now, using conditional statements, check if the typed word matches one of the words listed. 
# 5. If there is match, print the definition.

if word == "Programming Language":
    print("A set of instructions, rules, and syntax used to write programs that computers can understand.")
elif word == "Pseudocode":
    print("A plain English, informal description of the steps or logic of an algorithm.")
elif word == "Binary Number":
    print("A number expressed in the base-2 numeral system, using only 0 and 1.")
elif word == "Syntax":
    print("The set of rules that define the correct structure of code in a particular language.")
elif word == "Variable":
    print("A symbolic name that acts as a storage location in memory, holding a value.")
elif word == "Data Type":
    print("A classification that specifies what kind of value a variable can hold (e.g., numbers, text).")
elif word == "Whole Number":
    print("Non-negative numbers without fractional or decimal parts (0, 1, 2, 3...).")
elif word == "Integer Number":
    print("Numbers including all whole numbers and their negative counterparts, without decimals.")
elif word == "Logical operator":
    print("Special keywords (like and, or, not) used to combine or modify conditional statements.")
elif word == "Debugging":
    print("The process of identifying, analyzing, and fixing errors ('bugs') in code.")
else:
    print("Word not found in the list. Make sure to type it exactly as shown!")
