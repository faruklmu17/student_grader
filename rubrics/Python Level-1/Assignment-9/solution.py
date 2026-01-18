# Assignment 9: Lists and Indexing

# 1. What's a list in Python and how do you show what's in it?
# A list is a collection of items ordered in a sequence. You can store 
# different types of data in it. To see what's in it, you can simply 
# use the print() function.
my_list = [10, 20, 30]
print("List contents:", my_list)

# 2. Why are index numbers important in Python?
# Index numbers allow us to pinpoint and access specific items within a list. 
# Without them, we couldn't easily retrieve or change one piece of data. 
# Remember: Python indices start at 0!

# 3. List of five snacks and print only the third one
snacks = ["Chips", "Cookies", "Apple", "Chocolate", "Popcorn"]
# The third item is at index 2 (counting 0, 1, 2)
print("The third snack is:", snacks[2])

# 4. List with six decimal numbers and count items using len()
decimals = [1.1, 2.2, 3.3, 4.4, 5.5, 6.6]
print("The list has", len(decimals), "items.")

# 5. Print the last decimal number and check its data type
# We can use index -1 to get the last item
last_item = decimals[-1]
print("The last decimal is:", last_item)
print("The data type of the last item is:", type(last_item))

# 6. Turn a string into a list using the list() function
text = "Python"
char_list = list(text)
print("String converted to list:", char_list)

# 7. When does an IndexError happen and what does it mean?
# An IndexError happens when you try to access an index that is out of range. 
# For example, if a list has 3 items (indices 0, 1, 2) and you try to 
# access index 10, Python will throw an IndexError because that "slot" 
# doesn't exist.
