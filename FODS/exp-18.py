import pandas as pd
import matplotlib.pyplot as plt
from tkinter import Tk, filedialog

root = Tk()
root.withdraw()

file_path = filedialog.askopenfilename(
    title="Select exp-18.csv",
    filetypes=[("CSV files", "*.csv")]
)

df = pd.read_csv(file_path)

frequency = df["likes"].value_counts().sort_index()

print("\nFrequency Distribution of Likes:\n")

print(frequency)

plt.bar(
    frequency.index.astype(str),
    frequency.values,
    edgecolor="black"
)

plt.xlabel("Number of Likes")
plt.ylabel("Frequency")
plt.title("Frequency Distribution of Likes")
plt.tight_layout()
plt.show()
