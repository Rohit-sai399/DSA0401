import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier, plot_tree

iris = load_iris()

X = iris.data
y = iris.target

model = DecisionTreeClassifier(
    max_depth=4,
    random_state=42
)

model.fit(X, y)

sepal_length = float(input("Enter sepal length: "))
sepal_width = float(input("Enter sepal width: "))
petal_length = float(input("Enter petal length: "))
petal_width = float(input("Enter petal width: "))

new_flower = np.array([
    [
        sepal_length,
        sepal_width,
        petal_length,
        petal_width
    ]
])

prediction = model.predict(new_flower)[0]

probability = model.predict_proba(new_flower)[0]

print("\nPredicted Iris Species:",
      iris.target_names[prediction])

print(
    "Prediction Probability:",
    round(probability[prediction] * 100, 2),
    "%"
)

plt.figure(figsize=(14, 8))

plot_tree(
    model,
    feature_names=iris.feature_names,
    class_names=iris.target_names,
    filled=True,
    rounded=True
)

plt.title("Decision Tree for Iris Classification")
plt.show()

plt.figure()

plt.bar(
    iris.target_names,
    probability,
    edgecolor="black"
)

plt.xlabel("Species")
plt.ylabel("Probability")
plt.title("Prediction Probability for New Flower")
plt.show()
