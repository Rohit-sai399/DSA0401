import pandas as pd
import numpy as np
from tkinter import Tk
from tkinter.filedialog import askopenfilename
from scipy import stats

Tk().withdraw()

file = askopenfilename(
    title="Select Blood Pressure Dataset",
    filetypes=[("CSV Files", "*.csv")]
)

if not file:
    print("No file selected")
    exit()

df = pd.read_csv(file)

for group in ["Drug", "Placebo"]:

    data = df[df["Group"] == group]["Reduction"]

    n = len(data)
    mean = data.mean()
    sd = data.std()
    se = sd / np.sqrt(n)

    t_value = stats.t.ppf(0.975, n - 1)

    margin = t_value * se

    lower = mean - margin
    upper = mean + margin

    print("\nGroup:", group)
    print("Sample Size =", n)
    print("Mean Reduction =", round(mean, 2))
    print("95% Confidence Interval =",
          round(lower, 2), "to", round(upper, 2))
