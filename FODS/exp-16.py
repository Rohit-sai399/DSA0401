import re
import matplotlib.pyplot as plt
from collections import Counter
from tkinter import Tk, filedialog

root = Tk()
root.withdraw()

file_path = filedialog.askopenfilename(
    title="Select exp-16.txt",
    filetypes=[("Text files", "*.txt")]
)

with open(file_path, "r", encoding="utf-8") as file:
    text = file.read()

words = re.findall(r'\b[a-zA-Z]+\b', text.lower())

frequency = Counter(words)

print("\nWord Frequency Distribution:\n")

for word, count in frequency.most_common():
    print(word, ":", count)

top_words = frequency.most_common(10)

words_list = [x[0] for x in top_words]
counts = [x[1] for x in top_words]

plt.bar(words_list, counts, edgecolor="black")
plt.xlabel("Words")
plt.ylabel("Frequency")
plt.title("Top 10 Word Frequency Distribution")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
