# 1. Understanding of OOP
# Object-Oriented Programming (OOP) is a programming paradigm based on the concept of "objects," 
# which can contain data (attributes) and code (methods). It organizes software design 
# around data, or objects, rather than functions and logic.

# 2. Define a class and the process of creating one
# A class is a blueprint or template for creating objects. 
# To create a class in Python, use the 'class' keyword followed by the class name and a colon.
class Car:
    # 3. Significance of a class variable
    # A class variable is a variable that is shared by all instances of a class. 
    # It is defined within the class but outside any methods. 
    # It’s significant because it allows all objects of that class to share the same data.
    wheels = 4  # This is a class variable

    def __init__(self, make, model):
        self.make = make    # Instance variable
        self.model = model  # Instance variable

# 5. Concept of an object and steps to create one
# An object is an instance of a class. It is a concrete entity based on the class blueprint.
# To create an object:
# 1. Use the class name.
# 2. Follow it with parentheses (optionally passing arguments if __init__ requires them).
# 3. Assign the result to a variable.

# 6. Instantiate three objects based on the class in #4
car1 = Car("Toyota", "Camry")
car2 = Car("Tesla", "Model 3")
car3 = Car("Ford", "Mustang")

# 7. Demonstrate how to access class variables from the objects & print values
print(f"Car 1 wheels: {car1.wheels}")
print(f"Car 2 wheels: {car2.wheels}")
print(f"Car 3 wheels: {car3.wheels}")

# 8. Saving an accessed class variable into a new variable
# Yes, it is possible.
wheel_count = car1.wheels
print(f"The value stored in the new variable 'wheel_count' is: {wheel_count}")

# Example of updated usage:
print(f"Total wheels for car fleet: {wheel_count}")
