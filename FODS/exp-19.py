# Develop a Python program to calculate the frequency distribution of words in the customer
# reviews dataset?
import pandas as pd
import re
import matplotlib.pyplot as plt
from collections import Counter
from tkinter import Tk, filedialog

root = Tk()
root.withdraw()

file_path = filedialog.askopenfilename(
    title="Select exp-19.csv",
    filetypes=[("CSV files", "*.csv")]
)

df = pd.read_csv(file_path)

all_words = []

for review in df["review"].dropna():
    words = re.findall(
        r'\b[a-zA-Z]+\b',
        review.lower()
    )
    all_words.extend(words)

frequency = Counter(all_words)

print("\nWord Frequency Distribution:\n")

for word, count in frequency.most_common():
    print(word, ":", count)

top_words = frequency.most_common(10)

words_list = [x[0] for x in top_words]
counts = [x[1] for x in top_words]

plt.bar(
    words_list,
    counts,
    edgecolor="black"
)

plt.xlabel("Words")
plt.ylabel("Frequency")
plt.title("Top 10 Words in Customer Reviews")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
