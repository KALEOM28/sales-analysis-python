import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = {
    "product":["laptop","mobile","tablet","laptop","mobile"],
    "city":["pune","mumbai","pune","delhi","pune"],
    "sales":["50000","20000","15000","60000","22000"]
}

dp = pd.DataFrame(data)

print(dp.head())
print(dp.tail())
print(dp.shape)
print(dp.info())
print(dp.describe())
dp["sales"] = dp["sales"].astype(int)
print(dp)

print("total sales : ", dp["sales"].sum())
print("total citys : ", dp["city"].count())
print("total products : ", dp["product"].count())

print("sales by citys")
print(dp.groupby("city")["sales"].sum())

print(dp.dtypes)
print("Sales by Product:")
print(dp.groupby(["city","sales","product"]).size())
print(dp.groupby("product")["sales"].sum())

print(".....product_sales.....")
product_sales = dp.groupby("product")["sales"].sum()
print(product_sales)

product_sales.plot(kind="bar")

plt.title("Sales by Product")
plt.xlabel("Product")
plt.ylabel("Sales")
plt.show()

print(".....city_sales.....")
city_sales = dp.groupby("city")["sales"].sum()

print(city_sales)
city_sales.plot(kind="bar")

plt.title("Sales by City")
plt.xlabel("City")
plt.ylabel("Sales")

plt.show()

print(".....Top_product & city.....")

top_product = product_sales.idxmax()
top_city = city_sales.idxmax()

print("Top Selling Product:", top_product)
print("City with Highest Sales:", top_city)

plt.savefig("product_sales.png")
print("Insight: Laptop has highest sales")
print(dp.describe())









