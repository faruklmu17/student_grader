# Assignment 12 Reference Solution (Vending Machine Debugging)

print("Welcome to X’s vending machine\n")
print("Product  Price   Code")
print("KitKat   $2.50   1001")
print("Coke     $3.00   1002")
print("Pepsi    $3.00   1003")
print("Mars     $2.40   1004")

# Create all the variables here
kitkat_price = 2.50
coke_price = 3.00 # Fixed: Changed from 3 to 3.00 for consistency
pepsi_price = 3.00
mars_price = 2.40

# Product codes are saved in a list
product_codes = [1001, 1002, 1003, 1004]

# Loop to get a valid product code from the user
while True:
    print("Type a product code to continue...")
    # FIX: input() returns a string, so we must convert it to int to compare with product_codes
    user_input = input()
    if user_input.isdigit():
        user_code = int(user_input)
    else:
        print("Invalid input! Please enter a numeric code.")
        continue

    # checking if the code matches kitkat code
    if user_code == product_codes[0]:
        print(f"You have selected KitKat. Please pay ${kitkat_price:.2f}")
        break

    # checking if the code matches coke code
    elif user_code == product_codes[1]:
        print(f"You have selected Coke. Please pay ${coke_price:.2f}")
        break # Added break to exit loop

    # checking if the code matches pepsi code
    elif user_code == product_codes[2]: # FIX: Changed from == product_codes[1] to product_codes[2]
        print(f"You have selected Pepsi. Please pay ${pepsi_price:.2f}")
        break # Added break to exit loop

    # checking if the code matches mars code
    elif user_code == product_codes[3]:
        print(f"You have selected Mars. Please pay ${mars_price:.2f}")
        break # Added break to exit loop

    # in case of an invalid code
    else:
        print("Invalid code! Try again")

# reading the amount from the customer
# FIX: input() must be converted to float to handle decimals
print("\nPlease insert money:")
inserted_money = float(input())

# Logic to dispense product and calculate change based on the selected user_code

# KitKat
if user_code == product_codes[0]:
    if inserted_money == kitkat_price:
        print(f"You have inserted ${inserted_money:.2f}\nDispensing KitKat...")
    elif inserted_money > kitkat_price:
        # FIX: change_amount should be inserted - price, not +
        change_amount = inserted_money - kitkat_price
        print(f"You have inserted more than ${kitkat_price:.2f}\nDispensing KitKat...\nAlong with the change ${change_amount:.2f}")
    elif inserted_money < kitkat_price:
        # FIX: required_amount should be price - inserted
        required_amount = kitkat_price - inserted_money
        print(f"You have not inserted enough coins/cash. Put ${required_amount:.2f} to get the KitKat!")

# Coke
elif user_code == product_codes[1]:
    if inserted_money == coke_price:
        print(f"You have inserted ${inserted_money:.2f}\nDispensing Coke...")
    elif inserted_money > coke_price:
        # FIX: price used was pepsi_price instead of coke_price in the original defective version
        change_amount = inserted_money - coke_price
        print(f"You have inserted more than ${coke_price:.2f}\nDispensing Coke...\nAlong with the change ${change_amount:.2f}")
    elif inserted_money < coke_price:
        # FIX: corrected the -+ operator bug
        required_amount = coke_price - inserted_money
        print(f"You have not inserted enough coins/cash. Put ${required_amount:.2f} to get the Coke!")

# Pepsi
elif user_code == product_codes[2]:
    if inserted_money == pepsi_price:
        print(f"You have inserted ${inserted_money:.2f}\nDispensing Pepsi...")
    elif inserted_money > pepsi_price:
        change_amount = inserted_money - pepsi_price
        print(f"You have inserted more than ${pepsi_price:.2f}\nDispensing Pepsi...\nAlong with the change ${change_amount:.2f}")
    elif inserted_money < pepsi_price:
        # FIX: Changed multiplication (*) to subtraction (-)
        required_amount = pepsi_price - inserted_money
        print(f"You have not inserted enough coins/cash. Put ${required_amount:.2f} to get the Pepsi!")

# Mars
elif user_code == product_codes[3]:
    if inserted_money == mars_price:
        print(f"You have inserted ${inserted_money:.2f}\nDispensing Mars...")
    elif inserted_money > mars_price:
        # FIX: Changed division (/) to subtraction (-)
        change_amount = inserted_money - mars_price
        print(f"You have inserted more than ${mars_price:.2f}\nDispensing Mars...\nAlong with the change ${change_amount:.2f}")
    elif inserted_money < mars_price:
        # FIX: Added the missing condition for less than price
        required_amount = mars_price - inserted_money
        print(f"You have not inserted enough coins/cash. Put ${required_amount:.2f} to get the Mars!")