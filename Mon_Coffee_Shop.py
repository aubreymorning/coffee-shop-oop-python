"""
ITEC 2120 Project - Coffee Shop (Module 1)
Objective: Defines the Food, Customer, and ShoppingCart classes used by the
coffee shop program to track menu items, customers, and their orders.
"""

class Food:
    def __init__(self, foodName, foodPrice=0):
        self.foodName = foodName
        self.foodPrice = foodPrice

    def setFoodName(self, foodName):
        self.foodName = foodName

    def setFoodPrice(self, foodPrice):
        self.foodPrice = foodPrice

    def getFoodName(self):
        return self.foodName

    def getFoodPrice(self):
        return self.foodPrice


class Customer:
    def __init__(self, customerName):
        self.customerName = customerName

    def setCustomerName(self, customerName):
        self.customerName = customerName

    def getCustomerName(self):
        return self.customerName


class ShoppingCart(Customer):
    def __init__(self, customerName):
        super().__init__(customerName)
        self.item = []       # list of food NAMES (strings)
        self.quantity = []   # list of quantities, in sync with self.item

    def addItem(self, foodItem, quantity):
        self.item.append(foodItem)
        self.quantity.append(quantity)

    def getItemPrice(self, foodList, foodName):
        for foodItem in foodList:
            if foodItem.getFoodName() == foodName:
                return foodItem.getFoodPrice()
        return 0

    def balance(self, foodList):
        total = 0
        for i in range(len(self.item)):
            foodName = self.item[i]
            q = self.quantity[i]
            p = self.getItemPrice(foodList, foodName)
            total += p * q
        return total


if __name__ == "__main__":
    cupcake = Food("cupcake", 2.00)
    cappuccino = Food("cappuccino", 5.00)
    menuList = [cupcake, cappuccino]

    customer = Customer("Amal")
    cart = ShoppingCart(customer.getCustomerName())
    cart.addItem("cupcake", 2)
    cart.addItem("cappuccino", 1)

    total = cart.balance(menuList)
    print(f"The total price should be ${total:.2f}")