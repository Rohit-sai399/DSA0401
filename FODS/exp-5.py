import pandas as pd
import numpy as np
from tkinter import Tk
from tkinter.filedialog import askopenfilename

Tk().withdraw()

file_path = askopenfilename(
    title="Select Fuel Efficiency CSV File",
    filetypes=[("CSV Files", "*.csv")]
)

df = pd.read_csv(file_path)

fuel_efficiency = np.array(df["Fuel_Efficiency"])

average_efficiency = np.mean(fuel_efficiency)
percentage_improvement = ((fuel_efficiency[-1] - fuel_efficiency[0]) / fuel_efficiency[0]) * 100

print(df)
print("\nAverage Fuel Efficiency:", average_efficiency)
print("Percentage Improvement:", percentage_improvement, "%")
