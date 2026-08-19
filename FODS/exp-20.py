# Create a Python program that fulfills these requirements and helps your team gain insights
# from the customer feedback data.
import pandas as pd
import re
import matplotlib.pyplot as plt
from collections import Counter
from tkinter import Tk, filedialog

root = Tk()
root.withdraw()

file_path = filedialog.askopenfilename(
    title="Select exp-20.csv",
    filetypes=[("CSV files", "*.csv")]
)

df = pd.read_csv(file_path)

stop_words = {
    "the", "and", "is", "a", "an", "are", "am",
    "i", "it", "this", "that", "to", "of", "in",
    "for", "with", "on", "was", "were", "be",
    "very", "really", "its", "my", "our", "their",
    "has", "have", "had", "from", "as", "at",
    "by", "or", "but", "so", "not"
}

all_words = []

for feedback in df["feedback"].dropna():

    feedback = feedback.lower()

    words = re.findall(
        r'\b[a-zA-Z]+\b',
        feedback
    )

    words = [
        word for word in words
        if word not in stop_words
    ]

    all_words.extend(words)

frequency = Counter(all_words)

n = int(
    input("Enter the number of top words to display: ")
)

top_words = frequency.most_common(n)

print("\nTop", n, "Most Frequent Words:\n")

for word, count in top_words:
    print(word, ":", count)

words_list = [x[0] for x in top_words]
counts = [x[1] for x in top_words]

plt.bar(
    words_list,
    counts,
    edgecolor="black"
)

plt.xlabel("Words")
plt.ylabel("Frequency")
plt.title(
    "Top " + str(n) + " Most Frequent Words"
)

plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
