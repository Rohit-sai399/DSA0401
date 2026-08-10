import pandas as pd
import matplotlib.pyplot as plt
from tkinter import Tk
from tkinter.filedialog import askopenfilename
from scipy import stats

Tk().withdraw()

file = askopenfilename(
    title="Select Age and Body Fat Dataset",
    filetypes=[("CSV Files", "*.csv")]
)

if not file:
    print("No file selected")
    exit()

df = pd.read_csv(file)

print("DATA")
print(df)

print("\nSTATISTICS")

print("\nAge")
print("Mean =", df["age"].mean())
print("Median =", df["age"].median())
print("Standard Deviation =", df["age"].std())

print("\nBody Fat")
print("Mean =", df["%fat"].mean())
print("Median =", df["%fat"].median())
print("Standard Deviation =", df["%fat"].std())

plt.figure()
df[["age", "%fat"]].boxplot()
plt.title("Boxplot of Age and Body Fat")
plt.show()

plt.figure()
plt.scatter(df["age"], df["%fat"])
plt.xlabel("Age")
plt.ylabel("Body Fat %")
plt.title("Age vs Body Fat")
plt.grid()
plt.show()

plt.figure()
stats.probplot(df["age"], dist="norm", plot=plt)
plt.title("Q-Q Plot - Age")
plt.show()

plt.figure()
stats.probplot(df["%fat"], dist="norm", plot=plt)
plt.title("Q-Q Plot - Body Fat")
plt.show()
