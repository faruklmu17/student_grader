# Assignment-3 Python Level-2 Solution

# 1. Now make a list of five of your favourite snacks
snacks = ["Chips", "Chocolate", "Fruit", "Cookies", "Nuts"]

# 2. Only print the 3rd favourite snack from the list
# The 3rd item is at index 2
print("3rd favourite snack:", snacks[2])

# 3. From the same list, print the first three snacks using a for loop and then break out of the loop
print("\nFirst three snacks using a for loop:")
count = 0
for snack in snacks:
    print(snack)
    count += 1
    if count == 3:
        break

# 4. Print your name 10 times using a while loop. 
# But, each name should have a serial number starting from 1.
print("\nName printed 10 times:")
name = "Student Name"
i = 1
while i <= 10:
    print(f"{i}. {name}")
    i += 1

# 5. Print all the even numbers from 20 to 2 using a while loop. (Not from 2 to 20).
print("\nEven numbers from 20 to 2:")
num = 20
while num >= 2:
    print(num)
    num -= 2
