import pandas as pd
import matplotlib.pyplot as plt

study_hours = [1, 2, 3, 4, 5, 6, 7, 8]
scores = [35, 45, 50, 60, 68, 75, 85, 95]

df = pd.DataFrame({
    "Study Hours": study_hours,
    "Exam Scores": scores
})

print(df)

correlation = df["Study Hours"].corr(df["Exam Scores"])
print("\nCorrelation:", correlation)

plt.figure(figsize=(6,4))
plt.plot(study_hours, scores, marker="o")
plt.title("Study Hours vs Exam Scores (Line Plot)")
plt.xlabel("Study Hours")
plt.ylabel("Exam Scores")
plt.grid(True)
plt.show()

plt.figure(figsize=(6,4))
plt.scatter(study_hours, scores)
plt.title("Study Hours vs Exam Scores (Scatter Plot)")
plt.xlabel("Study Hours")
plt.ylabel("Exam Scores")
plt.grid(True)
plt.show()
