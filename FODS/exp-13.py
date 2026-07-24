import pandas as pd

data = {
    "Day": [1, 2, 3, 4, 5, 6, 7],
    "Close": [150, 152, 149, 155, 153, 156, 154]
}

df = pd.DataFrame(data)
df.to_csv("stock_data.csv", index=False)

stock = pd.read_csv("stock_data.csv")

print(stock)

print("\nMean Closing Price:", stock["Close"].mean())
print("Standard Deviation:", stock["Close"].std())
print("Highest Price:", stock["Close"].max())
print("Lowest Price:", stock["Close"].min())
print("Price Range:", stock["Close"].max() - stock["Close"].min())
