import numpy as np

sales_data = np.array([
    [100, 120, 110],
    [200, 210, 220],
    [150, 160, 170]
])

average_price = np.mean(sales_data)

print("Sales Data:")
print(sales_data)

print("\nAverage Price of All Products Sold =", average_price)
