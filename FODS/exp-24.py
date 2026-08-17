import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from tkinter import Tk, filedialog

root = Tk()
root.withdraw()

file_path = filedialog.askopenfilename(
    title="Select exp-24.csv",
    filetypes=[("CSV files", "*.csv")]
)

df = pd.read_csv(file_path)
data = df["concentration"].dropna().values

sample_size = int(input("Enter sample size: "))
confidence_level = float(input("Enter confidence level (%): "))
precision = float(input("Enter desired level of precision: "))

if sample_size > len(data):
    print("Sample size cannot be greater than the number of observations.")
else:
    sample = np.random.choice(data, sample_size, replace=False)

    sample_mean = np.mean(sample)
    sample_std = np.std(sample, ddof=1)
    standard_error = sample_std / np.sqrt(sample_size)

    if confidence_level == 90:
        z = 1.645
    elif confidence_level == 95:
        z = 1.96
    elif confidence_level == 99:
        z = 2.576
    else:
        z = 1.96

    margin_error = z * standard_error
    lower = sample_mean - margin_error
    upper = sample_mean + margin_error

    print("\nPoint Estimate:", round(sample_mean, 4))
    print("Confidence Level:", confidence_level, "%")
    print("Confidence Interval:", round(lower, 4), "to", round(upper, 4))
    print("Margin of Error:", round(margin_error, 4))

    if margin_error <= precision:
        print("Desired precision is achieved.")
    else:
        print("Desired precision is not achieved.")

    plt.hist(data, bins=10, edgecolor="black")
    plt.axvline(sample_mean, linestyle="--", linewidth=2, label="Sample Mean")
    plt.xlabel("Rare Element Concentration")
    plt.ylabel("Frequency")
    plt.title("Rare Element Concentration Distribution")
    plt.legend()
    plt.show()
