import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import ttest_ind
from tkinter import Tk, filedialog

root = Tk()
root.withdraw()

file_path = filedialog.askopenfilename(
    title="Select exp-26.csv",
    filetypes=[("CSV files", "*.csv")]
)

df = pd.read_csv(file_path)

control = df[df["group"] == "Control"]["result"]
treatment = df[df["group"] == "Treatment"]["result"]

control_mean = control.mean()
treatment_mean = treatment.mean()

t_stat, p_value = ttest_ind(
    treatment,
    control,
    equal_var=False
)

print("\nControl Group Mean:", round(control_mean, 3))
print("Treatment Group Mean:", round(treatment_mean, 3))
print("t-statistic:", round(t_stat, 4))
print("p-value:", round(p_value, 6))

alpha = 0.05

if p_value < alpha:
    print("Reject the null hypothesis.")
    print("The treatment has a statistically significant effect.")
else:
    print("Fail to reject the null hypothesis.")
    print("The treatment does not have a statistically significant effect.")

plt.boxplot(
    [control, treatment],
    tick_labels=["Control", "Treatment"]
)

plt.ylabel("Treatment Result")
plt.title("Control vs Treatment Group")
plt.show()

plt.bar(
    ["Control", "Treatment"],
    [control_mean, treatment_mean],
    edgecolor="black"
)

plt.ylabel("Mean Result")
plt.title("Mean Treatment Results")
plt.show()
