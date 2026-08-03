import pandas as pd
import matplotlib.pyplot as plt
from tkinter import Tk
from tkinter.filedialog import askopenfilename


Tk().withdraw()


file_path = askopenfilename(
    title="Select Sales Data CSV File",
    filetypes=[("CSV Files", "*.csv")]
)


df = pd.read_csv(file_path)

print(df)

plt.figure(figsize=(6,4))
plt.plot(df["Month"], df["Sales"], marker='o')
plt.title("Line Plot")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.grid(True)
plt.show()


plt.figure(figsize=(6,4))
plt.scatter(df["Month"], df["Sales"])
plt.title("Scatter Plot")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.grid(True)
plt.show()

plt.figure(figsize=(6,4))
plt.bar(df["Month"], df["Sales"])
plt.title("Bar Plot")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.show()
