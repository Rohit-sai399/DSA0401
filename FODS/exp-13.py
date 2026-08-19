# Your task is to build a Python program that reads the stock data from a CSV file, calculates
# the variability of stock prices, and provides insights into the stock's price movements.
import pandas as pd
from tkinter import Tk
from tkinter.filedialog import askopenfilename

Tk().withdraw()


file_path = askopenfilename(
    title="Select Stock Data CSV File",
    filetypes=[("CSV Files", "*.csv")]
)


stock = pd.read_csv(file_path)

print(stock)

print("\nMean Closing Price:", stock["Close"].mean())
print("Standard Deviation:", stock["Close"].std())
print("Highest Price:", stock["Close"].max())
print("Lowest Price:", stock["Close"].min())
print("Price Range:", stock["Close"].max() - stock["Close"].min())
