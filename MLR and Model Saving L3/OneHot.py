import pandas as pd
from sklearn.linear_model import LinearRegression

data=pd.read_csv("flat_price.csv")

features=data[["place","area"]]
target=data["price"]

new_features=pd.get_dummies(features)

model=LinearRegression()
model.fit(new_features.values,target)

area=float(input("Please enter the area"))
choice=int(input("1. Karjat 2 . Khandala 3. Lonavala"))

if choice==1:
    price=model.predict([[area,1,0,0]])
elif choice==2:
    price=model.predict([[area,0,1,0]])
elif choice ==3:
    price=model.predict([[area,0,0,1]])
else:
    print("Invalid")
    exit(0)

print("The price is ",price)
