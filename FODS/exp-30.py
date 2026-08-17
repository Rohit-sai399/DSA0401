import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler
from tkinter import Tk, filedialog

root = Tk()
root.withdraw()

file_path = filedialog.askopenfilename(
    title="Select exp-30.csv",
    filetypes=[("CSV files", "*.csv")]
)

df = pd.read_csv(file_path)

features = [
    "fever",
    "cough",
    "breathing_problem",
    "fatigue"
]

X = df[features]
y = df["condition"]

scaler = StandardScaler()

X_scaled = scaler.fit_transform(X)

k = int(input("Enter the value of k: "))

if k <= 0 or k > len(df):
    print("Invalid value of k.")
else:
    model = KNeighborsClassifier(
        n_neighbors=k
    )

    model.fit(X_scaled, y)

    fever = float(input("Enter fever (0 or 1): "))
    cough = float(input("Enter cough (0 or 1): "))
    breathing = float(
        input("Enter breathing problem (0 or 1): ")
    )
    fatigue = float(input("Enter fatigue (0 or 1): "))

    new_patient = np.array([
        [fever, cough, breathing, fatigue]
    ])

    new_patient_scaled = scaler.transform(
        new_patient
    )

    prediction = model.predict(
        new_patient_scaled
    )[0]

    probability = model.predict_proba(
        new_patient_scaled
    )[0]

    if prediction == 1:
        print(
            "\nPrediction: Patient has the medical condition."
        )
    else:
        print(
            "\nPrediction: Patient does not have the medical condition."
        )

    print(
        "Prediction Probability:",
        probability
    )

    counts = df["condition"].value_counts().sort_index()

    plt.bar(
        ["No Condition", "Condition"],
        counts.values,
        edgecolor="black"
    )

    plt.xlabel("Class")
    plt.ylabel("Number of Patients")
    plt.title("Patient Condition Distribution")
    plt.show()
