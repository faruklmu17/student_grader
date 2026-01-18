```python
print("Welcome to X’s vending machine\n")
print("Product  Price   Code")
print("KitKat   $2.50   1001")
print("Coke     $3.00   1002")
print("Pepsi    $3.00   1003")
print("Mars     $2.40   1004")

# Create all the variables here
kitkat_price = 2.50
coke_price = 3.00
pepsi_price = 3.00
mars_price = 2.40

# Product codes are saved in a list
product_codes = [1001, 1002, 1003, 1004]
product_names = ["KitKat", "Coke", "Pepsi", "Mars"]
product_prices = [kitkat_price, coke_price, pepsi_price, mars_price]

while True:
    # Ask the user to type a code
    print("Type a product code to continue...")
    # Read the code from the user
    user_code = int(input())

    # Check if the code is valid
    if user_code in product_codes:
        # Get the index of the product code
        index = product_codes.index(user_code)
        print(f"You have selected {product_names[index]}. Please pay ${product_prices[index]:.2f}")
        break
    else:
        print("Invalid code! Try again")

# Reading the amount from the customer
inserted_money = float(input("Enter the amount: "))

# Calculate the change or required money
if inserted_money < product_prices[index]:
    required_amount = product_prices[index] - inserted_money
    print(f"You have not inserted enough coins/cash. Put ${required_amount:.2f} to get the {product_names[index]}!")
elif inserted_money > product_prices[index]:
    change_amount = inserted_money - product_prices[index]
    print(f"You have inserted more than ${product_prices[index]:.2f}. Dispensing {product_names[index]}... Along with the change ${change_amount:.2f}")
else:
    print(f"You have inserted ${inserted_money:.2f}. Dispensing {product_names[index]}...")
```