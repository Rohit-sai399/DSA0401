import pandas as pd
from tkinter import Tk
from tkinter.filedialog import askopenfilename

Tk().withdraw()


file_path = askopenfilename(
    title="Select Temperature CSV File",
    filetypes=[("CSV Files", "*.csv")]
)

df = pd.read_csv(file_path)

print(df)

mean_temp = df.groupby("City")["Temperature"].mean()
std_temp = df.groupby("City")["Temperature"].std()
temp_range = df.groupby("City")["Temperature"].apply(lambda x: x.max() - x.min())

print("\nMean Temperature")
print(mean_temp)

print("\nStandard Deviation")
print(std_temp)

print("\nTemperature Range")
print(temp_range)

print("\nCity with Highest Temperature Range:", temp_range.idxmax())
print("City with Most Consistent Temperature:", std_temp.idxmin())
