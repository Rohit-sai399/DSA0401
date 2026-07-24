import matplotlib.pyplot as plt

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
sales = [120, 150, 180, 170, 200, 220]

# Line Plot
plt.figure(figsize=(6,4))
plt.plot(months, sales, marker='o')
plt.title("Monthly Sales - Line Plot")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.grid(True)
plt.show()

# Bar Plot
plt.figure(figsize=(6,4))
plt.bar(months, sales)
plt.title("Monthly Sales - Bar Plot")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.show()
