import pandas as pd
from tkinter import Tk
from tkinter.filedialog import askopenfilename

Tk().withdraw()

file_path = askopenfilename(
    title="Select Shopping Data CSV File",
    filetypes=[("CSV Files", "*.csv")]
)

df = pd.read_csv(file_path)

prices = df["Price"]
quantities = df["Quantity"]

discount_rate = 10
tax_rate = 5

subtotal = sum(prices * quantities)

discount = subtotal * (discount_rate / 100)
after_discount = subtotal - discount
tax = after_discount * (tax_rate / 100)

total_cost = after_discount + tax

print(df)
print("\nSubtotal:", subtotal)
print("Discount:", discount)
print("Tax:", tax)
print("Total Cost:", total_cost)
