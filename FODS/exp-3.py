import numpy as np
house_data = np.array([
    [3, 1500, 250000],
    [5, 2200, 450000],
    [6, 2800, 550000],
    [4, 1800, 300000],
    [5, 2400, 500000]
])

houses = house_data[house_data[:,0] > 4]
average_price = np.mean(houses[:,2])

print("Average Sale Price =", average_price)
