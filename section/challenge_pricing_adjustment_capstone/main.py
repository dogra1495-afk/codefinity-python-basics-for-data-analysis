grocery_inventory = {
    "Milk": ("Dairy", 3.50, 8),
    "Eggs": ("Dairy", 5.50, 30),
    "Bread": ("Bakery", 2.99, 15),
    "Apples": ("Produce", 1.50, 50)
}

eggs_price = grocery_inventory.get("Eggs")[1]

if eggs_price > 5:
    print("Eggs are too expensive, reducing the price by $1.")
    grocery_inventory.update({"Eggs": ("Dairy", 5.50 - 1, 30)})
else:
    print("The price of Eggs is reasonable.")

grocery_inventory["Tomatoes"] = ("Produce", 1.20, 30)
print(F"Inventory after adding Tomatoes: {grocery_inventory}")

milk_stock = grocery_inventory.get("Milk")[2]

if milk_stock < 10:
    print("Milk needs to be restocked. Increasing stock by 20 units.")
    grocery_inventory.update({"Milk": ("Dairy", 3.50, 8 + 20)})
else:
    print("Milk has sufficient stock.")

apples_price = grocery_inventory.get("Apples")[1]

if apples_price > 2:
    grocery_inventory.pop("Apples")
    print("Apples removed from inventory due to high price.")


print(F"Updated inventory: {grocery_inventory}")