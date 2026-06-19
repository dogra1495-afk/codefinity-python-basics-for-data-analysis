# Current inventory on shelf
shelf = ("apples", "oranges", "bananas", "apples", "grapes", "bananas", "apples")
apple_count = shelf.count("apples")
print(F"Number of Apples: {apple_count}")

banana_index = shelf.index("bananas")
print(F"First Banana Index: {banana_index}")

if apple_count < 5:
    print(F"Apples need to be restocked.")
else:
    print(F"Apples are sufficiently stocked.")

grapes_count = shelf.count("grapes")

if grapes_count <= 1:
    print(F"Grapes need to be restocked.")
else:
    print(F"Grapes are sufficiently stocked.")

if "oranges" in shelf:
    orange_index = shelf.index("oranges")
    print(F"Oranges are at index: {orange_index}")
else:
    print(F"Oranges are out of stock.")










