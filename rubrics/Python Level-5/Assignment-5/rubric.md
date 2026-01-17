# Grading Rubric: Assignment-5 (Object-Oriented Programming - Classes & Objects)

## Goal
The student must demonstrate an understanding of Object-Oriented Programming (OOP) fundamentals in Python, specifically focusing on classes, objects, and class variables.

## Requirements
The submission MUST include the following:

1. **OOP Understanding**:
   - A clear explanation of what Object-Oriented Programming (OOP) is.

2. **Class Definition**:
   - A definition of a "class."
   - An explanation of the process/syntax for creating a class in Python (using the `class` keyword).

3. **Class Variables**:
   - An explanation of the significance and purpose of class variables (shared among all instances).

4. **Class Implementation**:
   - A functional Python class of the student's choice.
   - The class must incorporate at least one relevant **class variable**.

5. **Object Concept**:
   - An explanation of what an "object" (instance) is.
   - Outline the steps to instantiate an object in Python.

6. **Instantiations**:
   - Creating at least **three** distinct objects (instances) from the class defined in requirement #4.

7. **Accessing Class Variables**:
   - Demonstration of accessing a class variable through the created objects.
   - Printing the retrieved values to the console.

8. **Variable Assignment**:
   - Explanation of whether an accessed class variable can be stored in a new variable.
   - A code example showing this process.

## Scoring (Total: 10 Points)
- **Conceptual Understanding (3 pts)**: Explanations of OOP, classes, objects, and class variables are accurate (Questions 1, 2, 3, 5, 8).
- **Implementation (4 pts)**: Class is correctly defined with class variables, and three objects are instantiated (Questions 4, 6).
- **Application & Demonstration (3 pts)**: Successfully accesses class variables through objects and demonstrates saving them to new variables (Questions 7, 8).

**Deductions:**
- -1 for each missing explanation or definition.
- -1 if less than three objects are instantiated.
- -2 if the class variable is incorrectly used as an instance variable (inside `__init__` without being defined at the class level).
- -3 if code contains syntax errors that prevent it from running.

## Grading Criteria
- **Pass**: Score >= 5/10.
- **Resubmit**: Score < 5/10.

## Common Mistakes & Feedback Guidance (RAG CHEAT SHEET)
If you see these specific errors, provide the corresponding feedback:

1. **Class vs Instance Variable Confusion**
   - *Error*: Defining a variable inside `__init__` and calling it a class variable.
   - *Feedback*: "Remember: A class variable is defined directly inside the class but outside any methods. Variables defined inside `__init__` using `self.` are instance variables, meaning they belong to a specific object, not the whole class."

2. **Incorrect Instantiation Syntax**
   - *Error*: Trying to create an object without parenthetical notation, e.g., `my_obj = MyClass`.
   - *Feedback*: "To create an object (instantiate), you must call the class like a function: `my_obj = MyClass()`. Without the parentheses, you are just assigning the class itself to a variable."

3. **Missing Explanations**
   - *Error*: Code is provided but theory questions (OOP, class variable significance) are ignored.
   - *Feedback*: "Don't forget to answer the theory questions! Understanding the 'why' is just as important as the 'how' in Object-Oriented Programming."

4. **Accessing Variables**
   - *Error*: Student thinks class variables can ONLY be accessed via the class name.
   - *Feedback*: "While class variables can be accessed via `ClassName.variable`, they can also be accessed through an instance (object) like `object.variable`. Both are valid, but they behave differently if you try to modify them!"
