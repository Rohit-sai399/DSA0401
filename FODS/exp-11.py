import matplotlib.pyplot as plt

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
sales = [300, 350, 400, 380, 450, 500]

# Line Plot
plt.figure(figsize=(6,4))
plt.plot(months, sales, marker='o')
plt.title("Line Plot")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.grid(True)
plt.show()

# Scatter Plot
plt.figure(figsize=(6,4))
plt.scatter(months, sales)
plt.title("Scatter Plot")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.grid(True)
plt.show()

# Bar Plot
plt.figure(figsize=(6,4))
plt.bar(months, sales)
plt.title("Bar Plot")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.show()
