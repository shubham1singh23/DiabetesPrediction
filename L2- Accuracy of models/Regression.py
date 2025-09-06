import pandas as pd
from sklearn.linear_model import LinearRegression

data=pd.read_csv("Code2 - Copy.csv")

# Remove the null rows  from the data (it is called as data cleaning as model does
# accept null values
print(data.isnull().sum())
data=data.dropna()
print(data.isnull().sum())

model=LinearRegression()
features=data[["years"]]
target=data["salary"]
model.fit(features.values,target)

year=int(input("Enter the year: "))

salary=model.predict([[year]])
print("The salary is ",salary)