# How would you use NumPy arrays to calculate the average score for each subject and
# determine the subject with the highest average score? Assume 4x4 matrix that stores marks of each
# student in given order.
import pandas as pd
import numpy as np
from tkinter import Tk
from tkinter.filedialog import askopenfilename

Tk().withdraw()

file_path = askopenfilename(
    title="Select Student Scores CSV File",
    filetypes=[("CSV Files", "*.csv")]
)

df = pd.read_csv(file_path)

student_scores = df.to_numpy()

subjects = list(df.columns)

average_scores = np.mean(student_scores, axis=0)

highest_index = np.argmax(average_scores)
highest_subject = subjects[highest_index]

print(df)

print("\nAverage Scores:")
for subject, avg in zip(subjects, average_scores):
    print(f"{subject}: {avg:.2f}")

print("\nSubject with Highest Average Score:", highest_subject)
print("Highest Average Score:", average_scores[highest_index])
