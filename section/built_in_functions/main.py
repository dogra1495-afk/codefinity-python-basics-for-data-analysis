# Dictionary of products with price and quantity sold as strings
products = {
    "Apple": ["1.20", "50"],   # "Item": [price, quantity sold]
    "Banana": ["0.50", "100"],
    "Cherry": ["2.50", "25"],
    "Mango": ["1.75", "40"]
}
total_sales_list = []

for product in products:
    price, quantity_sold = products[product]
    float_price = float(price)
    int_quantity_sold = int(quantity_sold)
    total_sales  = float_price * int_quantity_sold
    print(F"Total sales for {product}: ${total_sales}")
    total_sales_list.append(total_sales)
        
total_sum = sum(total_sales_list)
min_sales = min(total_sales_list)
max_sales = max(total_sales_list)

print(F"Total sum of all sales: ${total_sum}")
print(F"Minimum sales: ${min_sales}")
print(F"Maximum sales: ${max_sales}")

