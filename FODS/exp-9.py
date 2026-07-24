import pandas as pd

property_data = pd.DataFrame({
    "Property_ID":[101,102,103,104,105],
    "Location":["Chennai","Hyderabad","Chennai","Bangalore","Hyderabad"],
    "Bedrooms":[2,3,5,4,6],
    "Area_sqft":[1200,1500,2500,1800,3000],
    "Listing_Price":[5000000,6500000,8000000,7000000,9500000]
})

print(property_data.groupby("Location")["Listing_Price"].mean())

print(len(property_data[property_data["Bedrooms"]>4]))

print(property_data.loc[property_data["Area_sqft"].idxmax()])
