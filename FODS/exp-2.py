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

sales_data = df.to_numpy()

average_price = np.mean(sales_data)

print("Sales Data:")
print(sales_data)

print("\nAverage Price of All Products Sold =", average_price)
