import pandas as pd

order_data = pd.DataFrame({
    "Customer_ID": [101, 102, 101, 103, 102, 101],
    "Order_Date": ["2024-01-10", "2024-01-12", "2024-01-15", "2024-01-18", "2024-01-20", "2024-01-25"],
    "Product_Name": ["Laptop", "Mouse", "Mouse", "Keyboard", "Laptop", "Keyboard"],
    "Order_Quantity": [1, 2, 3, 1, 2, 4]
})


order_data["Order_Date"] = pd.to_datetime(order_data["Order_Date"])

orders_per_customer = order_data.groupby("Customer_ID").size()
print("Total Orders by Each Customer:")
print(orders_per_customer)

avg_quantity = order_data.groupby("Product_Name")["Order_Quantity"].mean()
print("\nAverage Order Quantity for Each Product:")
print(avg_quantity)
earliest_date = order_data["Order_Date"].min()
latest_date = order_data["Order_Date"].max()

print("\nEarliest Order Date:", earliest_date)
print("Latest Order Date:", latest_date)
