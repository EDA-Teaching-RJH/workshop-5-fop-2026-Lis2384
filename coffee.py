price = 75
moneyList = [5,10,20,50]

while price > 0:
    print(f"price: {price}p")
    coin = int(input("insert coin:"))

    if coin in moneyList:
        price -= coin
    else:
        print("insert valid coin")

print("thank you, dispensing coffee")

change = abs(price)
print(f"change owed: {change}p")