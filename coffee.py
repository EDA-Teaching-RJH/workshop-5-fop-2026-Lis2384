#**"statement of requirements"**

price = 75 # The total price of the drink
moneyList = [5,10,20,50] # The list of coins the machine will accept

while price > 0: 
    print(f"price: {price}p")
    coin = int(input("insert coin:")) # While the price is higher then 0 the code will prompt user to insert more coins

    if coin in moneyList:
        price -= coin # If the coin can be accepted it will subtract from the total
    else:
        print("insert valid coin") # If the coin cant be accepted the user will be prompted to insert a valid coin

print("thank you, dispensing coffee")

change = abs(price) 
print(f"change owed: {change}p") # The machine at the end of the while loop will print the value of anything passed 0