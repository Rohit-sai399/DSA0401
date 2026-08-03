import pandas as pd
from tkinter import Tk
from tkinter.filedialog import askopenfilename
import matplotlib.pyplot as plt

file_path = askopenfilename(
    title="Select a CSV File",
    filetypes=[("CSV Files", "*.csv")]
)


if file_path:
    order_data = pd.read_csv(file_path)

    order_data["Order_Date"] = pd.to_datetime(order_data["Order_Date"])


    orders_per_customer = order_data.groupby("Customer_ID").size()
    print("Total Orders by Each Customer:")
    print(orders_per_customer)

    avg_quantity = order_data.groupby("Product_Name")["Order_Quantity"].mean()
    print("\nAverage Order Quantity for Each Product:")
    print(avg_quantity)
    earliest_date = order_data["Order_Date"].min()
    latest_date = order_data["Order_Date"].max()

    print("\nEarliest Order Date:", earliest_date.date())
    print("Latest Order Date:", latest_date.date())
else:
    print("No file selected.")
orders_per_customer.plot(kind='bar', color='skyblue')

plt.title("Total Orders by Each Customer")
plt.xlabel("Customer ID")
plt.ylabel("Number of Orders")
plt.grid(axis='y')
plt.show()
Tk().withdraw()



