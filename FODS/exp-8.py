import pandas as pd
import matplotlib.pyplot as plt
from tkinter import Tk
from tkinter.filedialog import askopenfilename


Tk().withdraw()


file_path = askopenfilename(
    title="Select Sales CSV File",
    filetypes=[("CSV Files", "*.csv")]
)

if not file_path:
    print("No file selected.")
    exit()

sales_data = pd.read_csv(file_path)

print("\nUploaded Data:")
print(sales_data)
top_products = sales_data.groupby("Product")["Quantity"].sum().sort_values(ascending=False).head(5)


print("\nTop 5 Products Sold:")
print(top_products)


plt.figure(figsize=(8,5))
top_products.plot(kind='bar')

plt.title("Top 5 Products by Quantity Sold")
plt.xlabel("Product")
plt.ylabel("Total Quantity Sold")
plt.xticks(rotation=45)
plt.tight_layout()

plt.show()
