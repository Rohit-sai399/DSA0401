import pandas as pd
from tkinter import Tk
from tkinter.filedialog import askopenfilename

Tk().withdraw()

file_path = askopenfilename(
    title="Select Property Data CSV File",
    filetypes=[("CSV Files", "*.csv")]
)

property_data = pd.read_csv(file_path)

print(property_data.groupby("Location")["Listing_Price"].mean())

print(len(property_data[property_data["Bedrooms"] > 4]))

print(property_data.loc[property_data["Area_sqft"].idxmax()])
