
prices = [100, 200, 50]
quantities = [2, 1, 4]

discount_rate = 10   
tax_rate = 5         
subtotal = sum(p * q for p, q in zip(prices, quantities))

discount = subtotal * (discount_rate / 100)
after_discount = subtotal - discount
tax = after_discount * (tax_rate / 100)

total_cost = after_discount + tax

print("Subtotal:", subtotal)
print("Discount:", discount)
print("Tax:", tax)
print("Total Cost:", total_cost)
