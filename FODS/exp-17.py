# Develop a code in python to find the frequency distribution of the ages of the customers who
# have made a purchase in the past month.
import pandas as pd
import matplotlib.pyplot as plt
from tkinter import Tk, filedialog

root = Tk()
root.withdraw()

file_path = filedialog.askopenfilename(
    title="Select exp-17.csv",
    filetypes=[("CSV files", "*.csv")]
)

df = pd.read_csv(file_path)

frequency = df["age"].value_counts().sort_index()

print("\nFrequency Distribution of Customer Ages:\n")

print(frequency)

plt.bar(
    frequency.index.astype(str),
    frequency.values,
    edgecolor="black"
)

plt.xlabel("Age")
plt.ylabel("Frequency")
plt.title("Frequency Distribution of Customer Ages")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
