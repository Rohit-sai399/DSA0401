import numpy as np
student_scores = np.array([
    [85, 78, 92, 88],
    [90, 82, 85, 91],
    [76, 89, 80, 84],
    [88, 91, 87, 90]
])

subjects = ["Math", "Science", "English", "History"]

average_scores = np.mean(student_scores, axis=0)

highest_index = np.argmax(average_scores)
highest_subject = subjects[highest_index]

print("Average Scores:")
for subject, avg in zip(subjects, average_scores):
    print(f"{subject}: {avg:.2f}")

print("\nSubject with Highest Average Score:", highest_subject)
print("Highest Average Score:", average_scores[highest_index])
