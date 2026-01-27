# Rubric: Python Level-2 - Assignment 4

## Assignment Overview
In this assignment, students will update their initial vocabulary program (from Assignment 1) to incorporate loops. They will also create a more advanced version using Python lists, `for` loops, and the `random` module to provide a dynamic user experience.

---

## Part 1: Vocabulary List Update (Looping)
Update the program from Assignment 1 to include new terms and persist using a loop.

### 1. New Vocabulary Words (E)
- **Words to add**: "Loop" and "Module".
- **Requirements**:
    - "Loop" and "Module" must be included in the displayed list.
    - Definitions must be provided when selected.

### 2. Implementation of `while` Loop (M)
- **Functionality**: The program should not exit after a single word lookup.
- **Requirements**:
    - Use a `while` loop to wrap the input and lookup logic.
    - After showing a definition, it should return to the word list or ask for the next input.
    - Provide a way to exit the loop (optional but recommended).

---

## Part 2: Advanced Vocabulary List (`assignment_4-newVocabList.py`)
Create a new file using more advanced data structures.

### 3. Use of Python Lists and `for` Loops (E)
- **Requirements**:
    - Store all vocabulary words in a Python list.
    - Use a `for` loop to iterate through and print the list of words.

### 4. Random Word Feature (H)
- **Functionality**: Ask the user if they want to see a random word.
- **Requirements**:
    - Handle "yes" input: Show a random word and its corresponding definition. Loop back to the list/menu afterwards.
    - Handle "no" input: Print "Thank you for using the program!" and terminate.
    - Use the `random` module (e.g., `random.choice()`).

---

## Expected Output Example

```text
Word List:
- Programming Language
- Pseudocode
- Binary Number
- Syntax
- Variable
- Data Type
- Whole Number
- Integer Number
- Logical operator
- Debugging
- Loop
- Module

Would you like to see a random word and its definition? (yes/no): yes

Random Word: Loop
Definition: A sequence of instructions that is continually repeated until a certain condition is reached.

Word List:
- Programming Language
...
Would you like to see a random word and its definition? (yes/no): no
Thank you for using the program!
```

## Grading Criteria
| Requirement | Weight |
| :--- | :--- |
| Correct definitions for "Loop" and "Module" added | 15% |
| `while` loop implemented in original script (persistence) | 25% |
| Words stored in a List and printed via `for` loop | 20% |
| `random` module used to pick random vocab | 25% |
| "no" terminates with correct message | 10% |
| Code quality (variable naming, indentation) | 5% |
