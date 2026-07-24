import numpy as np

fuel_efficiency = np.array([20, 25, 30, 35])

average_efficiency = np.mean(fuel_efficiency)
percentage_improvement = ((fuel_efficiency[3] - fuel_efficiency[0]) / fuel_efficiency[0]) * 100

print("Average Fuel Efficiency:", average_efficiency)
print("Percentage Improvement:", percentage_improvement, "%")
