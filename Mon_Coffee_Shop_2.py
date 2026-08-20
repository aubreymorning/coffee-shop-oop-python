"""
ITEC 2120 Project - Coffee Shop (Module 2)
Objective: Reads the day's menu from inventory.txt, takes orders from
customers one at a time (until "quit" is entered as the customer name),
prints/writes each customer's balance, and reports total daily revenue.
"""

from Mon_Coffee_Shop import *

# ---- Part 1: build the list of Food objects from inventory.txt ----
f1 = open("inventory.txt")
inventoryStr = f1.read()
foodList = inventoryStr.strip().split("\n")

foodListObjects = []
for element in foodList:
    if element.strip() == "":
        continue
    tempList = element.split(", ")
    foodName = tempList[0]
    foodPrice = float(tempList[1])
    food1 = Food(foodName, foodPrice)
    foodListObjects.append(food1)
f1.close()

# ---- Part 2: take orders until the customer types "quit" ----
f2 = open("daily_transactions.txt", "a")
revenue = 0
print("Welcome to <Your Name>'s Coffee Shop")

while True:
    customerName = input("Take customer name (quit to cancel): ")
    if customerName.lower() == "quit":
        break

    customer1 = Customer(customerName)
    cart1 = ShoppingCart(customer1.getCustomerName())

    for element in foodListObjects:
        name = element.getFoodName()
        price = element.getFoodPrice()
        q = input(f"Enter quantity of {name} at ${price:.2f}: ")
        while not q.isdecimal():
            q = input(f"Enter a valid number. Enter quantity of {name} at ${price:.2f}: ")
        if int(q) > 0:
            cart1.addItem(name, int(q))

    total = cart1.balance(foodListObjects)
    print(f"{customerName}, your balance is ${total:.2f}")
    f2.write(f"{customerName}, your balance is ${total:.2f}\n")

    revenue += total

print(f"Total Revenue for today is ${revenue:.2f}")
f2.write(f"Total Revenue for today is ${revenue:.2f}\n")
print("End of Program.")

f2.close()