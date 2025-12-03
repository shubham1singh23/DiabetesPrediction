import pandas as pd
from sklearn.linear_model import LinearRegression

data=pd.read_csv("Code1 (1).csv")
data[["area","bedrooms"]]=data["info"].str.split(",",expand=True)
features=data[["area","bedrooms"]]
target=data["price"]

model=LinearRegression()
model.fit(features.values,target)

area=float(input("Enter the area : "))
bedrooms=int(input("Enter the bedrooms : "))

result=model.predict([[area,bedrooms]])
print(result)