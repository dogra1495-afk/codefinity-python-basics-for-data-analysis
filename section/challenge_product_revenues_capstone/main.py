def calculate_revenue(prices, quantities_sold):
    revenue = []
    # 2. Compute each revenue and append
    for i in range(len(prices)):
        revenue.append(prices[i] * quantities_sold[i])
    return revenue

def formatted_output(revenues):
    sorted_list = sorted(revenues, key=lambda pr: pr[0].lower())
    for product, rev in sorted_list:
        print(f"{product} has total revenue of ${rev}")

# List of products, their prices, and the quantities sold
products = ["Bread", "Apples", "Oranges", "Bananas"]
prices = [0.50, 1.20, 2.50, 2.00]  # price per item
quantities_sold = [150, 200, 100, 50]  # number of items sold

revenue = calculate_revenue(prices, quantities_sold)

revenue_per_product = list(zip(products, revenue))

formatted_output(revenue_per_product)

