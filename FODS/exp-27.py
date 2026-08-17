import pandas as pd
import matplotlib.pyplot as plt
from tkinter import Tk, filedialog

root = Tk()
root.withdraw()

file_path = filedialog.askopenfilename(
    title="Select exp-27.csv",
    filetypes=[("CSV files", "*.csv")]
)

df = pd.read_csv(file_path)

top_goals = df.sort_values(
    by="goals",
    ascending=False
).head(5)

top_salary = df.sort_values(
    by="weekly_salary",
    ascending=False
).head(5)

average_age = df["age"].mean()

above_average = df[df["age"] > average_age]

print("\nTop 5 Players by Goals:")
print(top_goals[["name", "goals"]].to_string(index=False))

print("\nTop 5 Players by Weekly Salary:")
print(top_salary[["name", "weekly_salary"]].to_string(index=False))

print("\nAverage Age:", round(average_age, 2))

print("\nPlayers Above Average Age:")
print(above_average[["name", "age"]].to_string(index=False))

position_count = df["position"].value_counts()

plt.bar(
    position_count.index,
    position_count.values,
    edgecolor="black"
)

plt.xlabel("Position")
plt.ylabel("Number of Players")
plt.title("Distribution of Players by Position")
plt.show()
