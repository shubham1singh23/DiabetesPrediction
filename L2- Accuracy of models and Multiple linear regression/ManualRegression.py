import pandas as pd
from sklearn.linear_model import LinearRegression

data=pd.read_csv("Code2 - Copy.csv")

print(data.isnull().sum())
data=data.dropna()
print(data.isnull().sum())

model=LinearRegression()
features=data[["years"]]
target=data["salary"]
model.fit(features.values,target)

year=int(input("Enter the year: "))

m=model.coef_
c=model.intercept_
salary=m*year+c
print("The salary is ",salary)