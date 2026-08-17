import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from tkinter import Tk, filedialog

root = Tk()
root.withdraw()

file_path = filedialog.askopenfilename(
    title="Select exp-25.csv",
    filetypes=[("CSV files", "*.csv")]
)

df = pd.read_csv(file_path)

ratings = df["rating"].dropna()

mean_rating = ratings.mean()
std_rating = ratings.std()
n = len(ratings)

confidence_level = float(input("Enter confidence level (%): "))

if confidence_level == 90:
    z = 1.645
elif confidence_level == 95:
    z = 1.96
elif confidence_level == 99:
    z = 2.576
else:
    z = 1.96

margin_error = z * (std_rating / np.sqrt(n))

lower = mean_rating - margin_error
upper = mean_rating + margin_error

print("\nAverage Rating:", round(mean_rating, 3))
print("Confidence Level:", confidence_level, "%")
print("Confidence Interval:", round(lower, 3), "to", round(upper, 3))
print("Margin of Error:", round(margin_error, 3))

if mean_rating >= 4:
    print("Customer Satisfaction Level: High")
elif mean_rating >= 3:
    print("Customer Satisfaction Level: Moderate")
else:
    print("Customer Satisfaction Level: Low")

plt.hist(ratings, bins=6, edgecolor="black")
plt.axvline(mean_rating, linestyle="--", linewidth=2, label="Average Rating")
plt.xlabel("Rating")
plt.ylabel("Number of Reviews")
plt.title("Customer Rating Distribution")
plt.legend()
plt.show()
