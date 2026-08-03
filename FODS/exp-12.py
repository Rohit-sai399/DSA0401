import pandas as pd
import matplotlib.pyplot as plt
from tkinter import Tk
from tkinter.filedialog import askopenfilename


Tk().withdraw()

file_path = askopenfilename(
    title="Select Weather Data CSV File",
    filetypes=[("CSV Files", "*.csv")]
)

df = pd.read_csv(file_path)

print(df)


plt.figure(figsize=(6,4))
plt.plot(df["Month"], df["Temperature"], marker='o')
plt.title("Monthly Temperature")
plt.xlabel("Month")
plt.ylabel("Temperature (°C)")
plt.grid(True)
plt.show()

plt.figure(figsize=(6,4))
plt.scatter(df["Month"], df["Rainfall"])
plt.title("Monthly Rainfall")
plt.xlabel("Month")
plt.ylabel("Rainfall (mm)")
plt.grid(True)
plt.show()
