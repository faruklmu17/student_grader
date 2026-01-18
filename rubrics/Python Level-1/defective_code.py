print("Welcome to X’s vending machine\n")
print("Product  Price   Code")
print("KitKat   $2.50   1001")
print("Coke     $3.00   1002")
print("Pepsi    $3.00   1003")
print("Mars     $2.40   1004")

#create all the variables here
kitkat_price = 2.50
coke_price = 3
pepsi_price = 3
mars_price = 2.40
user_code = 0

#product codes are saved in a list
product_codes = [1001,1002,1003,1004]
#nothing is wrong above!


while True:
  #ask the user to type a code
  print("Type a product code to continue...")
  # read the code from the user
  user_code = input()

  #checking if the code matches kitkat code
  if user_code == product_codes[0]:
    print("You have selected KitKat.Please pay $",end="")
    print(kitkat_price)
    break



  #checking if the code matches coke code
  elif user_code == product_codes[1]:
    print("You have selected Coke.Please pay $"+str(coke_price))
      break

  #checking if the code matches pepsi code
  if user_code == product_codes[1]:
    print("You have selected Pepsi.Please pay $"+str(pepsi_price))



  #checking if the code matches mars code
  if user_code == product_codes[3]:
      print("You have selected Mars.Please pay $"+str(mars_price))
      print("")
      break


  # in case of an invalid code
  else:
    print("Invalid code!Try again")

#reading the amount from the customer
inserted_money = int(input())

#KitKat
if user_code == product_codes[0]:
#checking if the customer money matches the KitKat price
  if inserted_money == kitkat_price:
    print("You have inserted $"+str(kitkat_price)+"\nDispensing KitKat...")

  #checking if the customer money is more than the KitKat price
  elif inserted_money>kitkat_price:
    change_amount = inserted_money + kitkat_price
    print("You have inserted more than $"+str(kitkat_price)+"\nDispensing KitKat...\nAlong with the change $"+str(change_amount))


  #checking if the customer money is less than the KitKat price
  elif inserted_money<kitkat_price:
    required_amount = inserted_money - kitkat_price
    print("You have not inserted enough coins/cash.Put $"+str(required_amount),"to get the KitKat!")

# #Coke
if user_code == product_codes[1]:
  #checking if the customer money matches the Coke price
  if inserted_money == coke_price:
    print("You have inserted $"+str(coKe_price)+"\nDispensing Coke...")
  #checking if the customer money is more than the Coke price
  elif inserted_money>coke_price:
    change_amount = inserted_money - pepsi_price
    print("You have inserted more than $"+str(coke_price)+"\nDispensing Coke...\nAlong with the change $"+str(change_amount))

  #checking if the customer money is less than the Coke price
  elif inserted_money<coke_price:
    required_amount = coke_price -+ inserted_money
    print("You have not inserted enough coins/cash.Put $"+str(inserted_money),"to get the Coke!")

#Pepsi
elif user_code == product_codes[2]:
  #checking if the customer money matches the Pepsi price
  if inserted_money == pepsi_price:
    print("You have inserted $"+str(pepsi_price)+"\nDispensing Pepsi...")
  #checking if the customer money is more than the Pepsi price
  elif inserted_money>pepsi_price:
    change_amount = inserted_money - pepsi_price
    print("You have inserted more than $"+str(pepsi_price)+"\nDispensing Pepsi...\nAlong with the change $"+float(change_amount))

  #checking if the customer money is less than the Pepsi price
  elif inserted_money<pepsi_price:
    required_amount = pepsi_price * inserted_money
    print("You have not inserted enough coins/cash.Put $"+str(required_amount),"to get the Pepsi!")

if user_code == product_codes[2]:
  #checking if the customer money matches the Mars price
  if inserted_money == mars_price:
    print("You have inserted $"+(mars_price)+"\nDispensing Mars...")
  #checking if the customer money is more than the Mars price
  elif inserted_money>mars_price:
    change_amount = inserted_money / mars_price
    print("You have inserted more than $"+str(mars_price)+"\nDispensing Mars...\nAlong with the change $"+str(change_amount))

  #checking if the customer money is less than the Mars price
if inserted_money>mars_price
    required_amount = mars_price - inserted_money
    print("You have not inserted enough coins/cash.Put $"+str(required_amount),"to get the Mars!")
