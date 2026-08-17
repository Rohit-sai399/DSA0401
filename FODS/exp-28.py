import pandas as pd
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeRegressor, plot_tree
from tkinter import Tk, filedialog

root = Tk()
root.withdraw()

file_path = filedialog.askopenfilename(
    title="Select exp-28.csv",
    filetypes=[("CSV files", "*.csv")]
)

df = pd.read_csv(file_path)

features = [
    "mileage",
    "age",
    "brand",
    "engine_type"
]

X = df[features]
y = df["price"]

model = DecisionTreeRegressor(
    max_depth=4,
    random_state=42
)

model.fit(X, y)

mileage = float(input("Enter mileage: "))
age = float(input("Enter car age: "))
brand = float(input("Enter brand number (1, 2 or 3): "))
engine_type = float(input("Enter engine type (1 or 2): "))

new_car = pd.DataFrame(
    [[mileage, age, brand, engine_type]],
    columns=features
)

prediction = model.predict(new_car)[0]

print("\nPredicted Car Price:", round(prediction, 2))

node_indicator = model.decision_path(new_car)
leaf_id = model.apply(new_car)

print("\nDecision Path:")

tree = model.tree_

node_index = node_indicator.indices[
    node_indicator.indptr[0]:
    node_indicator.indptr[1]
]

for node_id in node_index:
    if node_id == leaf_id[0]:
        print("Reached prediction node.")
        continue

    feature = tree.feature[node_id]
    threshold = tree.threshold[node_id]
    value = new_car.iloc[0, feature]

    if value <= threshold:
        print(
            features[feature],
            "<=",
            round(threshold, 2)
        )
    else:
        print(
            features[feature],
            ">",
            round(threshold, 2)
        )

plt.figure(figsize=(14, 8))

plot_tree(
    model,
    feature_names=features,
    filled=True,
    rounded=True
)

plt.title("CART Decision Tree for Car Price Prediction")
plt.show()
