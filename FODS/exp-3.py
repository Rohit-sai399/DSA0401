import pandas as pd
import numpy as np
from tkinter import Tk
from tkinter.filedialog import askopenfilename

Tk().withdraw()

file_path = askopenfilename(
    title="Select House Data CSV File",
    filetypes=[("CSV Files", "*.csv")]
)

df = pd.read_csv(file_path)

house_data = df.to_numpy()

houses = house_data[house_data[:, 0] > 4]
average_price = np.mean(houses[:, 2])

print(df)
print("\nAverage Sale Price =", average_price)
