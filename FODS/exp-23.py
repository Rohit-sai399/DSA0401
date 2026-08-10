import pandas as pd
from tkinter import Tk
from tkinter.filedialog import askopenfilename
from scipy.stats import ttest_ind

Tk().withdraw()

file = askopenfilename(
    title="Select A/B Test Dataset",
    filetypes=[("CSV Files", "*.csv")]
)

if not file:
    print("No file selected")
    exit()

df = pd.read_csv(file)

A = df[df["Design"] == "A"]["ConversionRate"]
B = df[df["Design"] == "B"]["ConversionRate"]

print("Mean Conversion Rate - Design A:", A.mean())
print("Mean Conversion Rate - Design B:", B.mean())

t_stat, p_value = ttest_ind(A, B)

print("\nT-statistic =", round(t_stat, 4))
print("P-value =", round(p_value, 6))

if p_value < 0.05:
    print("\nThere is a statistically significant difference.")
else:
    print("\nThere is no statistically significant difference.")
