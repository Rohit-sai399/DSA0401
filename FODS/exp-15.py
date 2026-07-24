import pandas as pd

data = {
    "City": [
        "Chennai", "Chennai", "Chennai",
        "Delhi", "Delhi", "Delhi",
        "Mumbai", "Mumbai", "Mumbai"
    ],
    "Temperature": [
        32, 34, 31,
        25, 30, 28,
        29, 30, 31
    ]
}

df = pd.DataFrame(data)

print(df)

mean_temp = df.groupby("City")["Temperature"].mean()
std_temp = df.groupby("City")["Temperature"].std()
temp_range = df.groupby("City")["Temperature"].apply(lambda x: x.max() - x.min())

print("\nMean Temperature")
print(mean_temp)

print("\nStandard Deviation")
print(std_temp)

print("\nTemperature Range")
print(temp_range)

print("\nCity with Highest Temperature Range:", temp_range.idxmax())
print("City with Most Consistent Temperature:", std_temp.idxmin())
