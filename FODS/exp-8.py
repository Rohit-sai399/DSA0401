import pandas as pd

# Sample DataFrame
sales_data = pd.DataFrame({
    "Product": ["Laptop", "Mouse", "Laptop", "Keyboard", "Mouse", "Laptop", "Keyboard", "Monitor"],
    "Quantity": [5, 10, 8, 6, 7, 9, 4, 3]
})

# Top 5 products sold the most
top_products = sales_data.groupby("Product")["Quantity"].sum().sort_values(ascending=False).head(5)

print(top_products)
