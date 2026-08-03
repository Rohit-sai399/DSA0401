import pandas as pd
import matplotlib.pyplot as plt
from tkinter import Tk
from tkinter.filedialog import askopenfilename


Tk().withdraw()


file_path = askopenfilename(
    title="Select CSV File",
    filetypes=[("CSV Files", "*.csv")]
)


df = pd.read_csv(file_path)

print(df)


correlation = df["Study Hours"].corr(df["Exam Scores"])
print("\nCorrelation:", correlation)

plt.figure(figsize=(6,4))
plt.plot(df["Study Hours"], df["Exam Scores"], marker="o")
plt.title("Study Hours vs Exam Scores (Line Plot)")
plt.xlabel("Study Hours")
plt.ylabel("Exam Scores")
plt.grid(True)
plt.show()

plt.figure(figsize=(6,4))
plt.scatter(df["Study Hours"], df["Exam Scores"])
plt.title("Study Hours vs Exam Scores (Scatter Plot)")
plt.xlabel("Study Hours")
plt.ylabel("Exam Scores")
plt.grid(True)
plt.show()
