# Coffee Shop Order & Revenue Tracker

A simple object-oriented Python program that helps a coffee shop owner take
customer orders and track daily revenue. Built for ITEC 2120 (Spring 2025).

## What it does

1. Reads a list of menu items and prices from `inventory.txt` and builds a
   list of `Food` objects.
2. Prompts for a customer's name, then asks how many of each menu item
   they'd like to buy (with input validation).
3. Calculates and displays the customer's balance, and appends it to
   `daily_transactions.txt`.
4. Repeats for the next customer until `"quit"` is entered as the name.
5. Prints and logs the total revenue for the day.

## Project structure

```
.
├── Mon_Coffee_Shop.py         # Module 1 — class definitions (Food, Customer, ShoppingCart)
├── Mon_Coffee_Shop_2.py       # Module 2 — implementation / program entry point
├── inventory.txt              # Menu items and prices (input file)
└── daily_transactions.txt     # Order log and daily revenue (generated/appended)
```

## Classes

**`Food`**
- Attributes: `foodName`, `foodPrice` (default `0`)
- Methods: `setFoodName`, `setFoodPrice`, `getFoodName`, `getFoodPrice`

**`Customer`**
- Attribute: `customerName`
- Methods: `setCustomerName`, `getCustomerName`

**`ShoppingCart`** (subclass of `Customer`)
- Attributes: `item` (list of food names), `quantity` (list of quantities, kept in sync with `item`)
- Methods:
  - `addItem(foodItem, quantity)` — records an item and its quantity
  - `getItemPrice(foodList, foodName)` — looks up a food's price from the menu; returns `0` if not found
  - `balance(foodList)` — computes the total cost of everything in the cart

## Setup

`inventory.txt` should have one item per line, formatted as:

```
cupcake, 2.00
cappuccino, 5.00
```

## Running it

```bash
python3 Mon_Coffee_Shop_2.py
```

Make sure `inventory.txt` is in the same directory. `daily_transactions.txt`
will be created (or appended to) automatically.

## Example

```
Welcome to <Your Name>'s Coffee Shop
Take customer name (quit to cancel): Sam
Enter quantity of cupcake at $2.00: 2
Enter quantity of cappuccino at $5.00: 1
Sam, your balance is $9.00
Take customer name (quit to cancel): quit
Total Revenue for today is $9.00
End of Program.
```

## Author

`<Your Name>` — ITEC 2120, Spring 2025
