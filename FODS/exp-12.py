import matplotlib.pyplot as plt

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
temperature = [22, 24, 28, 32, 35, 33]
rainfall = [20, 30, 60, 80, 120, 150]

# Line Plot
plt.figure(figsize=(6,4))
plt.plot(months, temperature, marker='o')
plt.title("Monthly Temperature")
plt.xlabel("Month")
plt.ylabel("Temperature (°C)")
plt.grid(True)
plt.show()

# Scatter Plot
plt.figure(figsize=(6,4))
plt.scatter(months, rainfall)
plt.title("Monthly Rainfall")
plt.xlabel("Month")
plt.ylabel("Rainfall (mm)")
plt.grid(True)
plt.show()
