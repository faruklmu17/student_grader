# Assignment 4 - Level 2 Python Solution

"""
PART 1: UPDATED VOCAB LIST WITH WHILE LOOP
Updating Assignment 1 with "Loop" and "Module"
"""

def update_assignment_1():
    while True:
        print("\n--- Vocabulary List ---")
        print("1. Programming Language")
        print("2. Pseudocode")
        print("3. Binary Number")
        print("4. Syntax")
        print("5. Variable")
        print("6. Data Type")
        print("7. Whole Number")
        print("8. Integer Number")
        print("9. Logical operator")
        print("10. Debugging")
        print("11. Loop")
        print("12. Module")
        print("-----------------------")
        
        word = input("Type a word to see its definition (or 'off' to stop): ").strip()
        
        if word.lower() == 'off':
            print("Exiting original vocabulary program...")
            break
            
        if word == "Programming Language":
            print("Definition: A set of instructions, rules, and syntax used to write programs that computers can understand.")
        elif word == "Pseudocode":
            print("Definition: A plain English, informal description of the steps or logic of an algorithm.")
        elif word == "Binary Number":
            print("Definition: A number expressed in the base-2 numeral system, using only 0 and 1.")
        elif word == "Syntax":
            print("Definition: The set of rules that define the correct structure of code in a particular language.")
        elif word == "Variable":
            print("Definition: A symbolic name that acts as a storage location in memory, holding a value.")
        elif word == "Data Type":
            print("Definition: A classification that specifies what kind of value a variable can hold (e.g., numbers, text).")
        elif word == "Whole Number":
            print("Definition: Non-negative numbers without fractional or decimal parts (0, 1, 2, 3...).")
        elif word == "Integer Number":
            print("Definition: Numbers including all whole numbers and their negative counterparts, without decimals.")
        elif word == "Logical operator":
            print("Definition: Special keywords (like and, or, not) used to combine or modify conditional statements.")
        elif word == "Debugging":
            print("Definition: The process of identifying, analyzing, and fixing errors ('bugs') in code.")
        elif word == "Loop":
            print("Definition: A sequence of instructions that is continually repeated until a certain condition is reached.")
        elif word == "Module":
            print("Definition: A file containing Python code that can be imported and used in other programs.")
        else:
            print("Word not found. Please check your spelling and capitalization.")

"""
PART 2: assignment_4-newVocabList.py
Using Lists, For Loops, and Random
"""

import random

def new_vocab_list_program():
    # Using a list to save all words
    words = [
        "Programming Language", "Pseudocode", "Binary Number", "Syntax", 
        "Variable", "Data Type", "Whole Number", "Integer Number", 
        "Logical operator", "Debugging", "Loop", "Module"
    ]
    
    # Dictionary for easy lookup
    definitions = {
        "Programming Language": "A set of instructions, rules, and syntax used to write programs that computers can understand.",
        "Pseudocode": "A plain English, informal description of the steps or logic of an algorithm.",
        "Binary Number": "A number expressed in the base-2 numeral system, using only 0 and 1.",
        "Syntax": "The set of rules that define the correct structure of code in a particular language.",
        "Variable": "A symbolic name that acts as a storage location in memory, holding a value.",
        "Data Type": "A classification that specifies what kind of value a variable can hold (e.g., numbers, text).",
        "Whole Number": "Non-negative numbers without fractional or decimal parts (0, 1, 2, 3...).",
        "Integer Number": "Numbers including all whole numbers and their negative counterparts, without decimals.",
        "Logical operator": "Special keywords (like and, or, not) used to combine or modify conditional statements.",
        "Debugging": "The process of identifying, analyzing, and fixing errors ('bugs') in code.",
        "Loop": "A sequence of instructions that is continually repeated until a certain condition is reached.",
        "Module": "A file containing Python code that can be imported and used in other programs."
    }

    while True:
        print("\n--- Available Words ---")
        # Printing the list using a for loop
        for w in words:
            print(f"- {w}")
            
        choice = input("\nWould you like to see a random word and its definition? (yes/no): ").lower().strip()
        
        if choice == "yes":
            random_word = random.choice(words)
            print(f"\nRandom Word: {random_word}")
            print(f"Definition: {definitions[random_word]}")
        elif choice == "no":
            print("Thank you for using the program!")
            break
        else:
            print("Invalid input! Please type 'yes' or 'no'.")

# If running this file directly, start Part 2 (the new assignment)
if __name__ == "__main__":
    print("Welcome to Assignment 4 Solutions")
    # You can choose which one to run
    new_vocab_list_program()
