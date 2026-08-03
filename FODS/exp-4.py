import pandas as pd
import numpy as np
from tkinter import Tk
from tkinter.filedialog import askopenfilename

Tk().withdraw()

file_path = askopenfilename(
    title="Select Sales Data CSV File",
    filetypes=[("CSV Files", "*.csv")]
)

df = pd.read_csv(file_path)

sales_data = np.array(df["Sales"])

total_sales = np.sum(sales_data)

percentage_increase = ((sales_data[-1] - sales_data[0]) / sales_data[0]) * 100

print(df)
print("\nTotal Sales:", total_sales)
print("Percentage Increase:", percentage_increase, "%")
