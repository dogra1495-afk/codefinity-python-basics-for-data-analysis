def apply_discount(price, discount=0.05):
    discounted_price = price * (1 - discount)
    return discounted_price

def apply_tax(price, tax=0.07):
    tax_price = price * (1 + tax)
    return tax_price

def calculate_total(price, discount=0.05, tax=0.07):
    discounted = apply_discount(price, discount)
    final_price = apply_tax(discounted, tax)
    return final_price

total_price_default = calculate_total(120)
total_price_custom = calculate_total(100, discount=0.10, tax=0.08)

print(F"Total cost with default discount and tax: ${total_price_default}")
print(F"Total cost with custom discount and tax: ${total_price_custom}")
