import pandas as pd
from sklearn.linear_model import LinearRegression

data=pd.read_csv('Code3.csv')

# ADD MULTIPLE FEATURES
features=data[["area","bedrooms"]]
target=data["price"]

model=LinearRegression()
model.fit(features.values,target)

area=float(input("Enter the area of interest: "))
bedrooms=float(input("Enter the number of bedrooms: "))
price=model.predict([[area,bedrooms]])

# Using coefficent and intercept
# price=model.predict([area,bedrooms])
# m1=model.coef_[0]
# m2=model.coef_[1]
# c=model.intercept_
# price=m1*area+m2*bedrooms+c

print("The price of the area is: ",price)