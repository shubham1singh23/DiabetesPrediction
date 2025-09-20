import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from pickle import *

data=pd.read_csv("Code3.csv")
features=data[["area","bedrooms"]]
target=data["price"]

x_train,x_test,y_train,y_test=train_test_split(features.values,target)


model=LinearRegression()
model.fit(x_train,y_train)

train_score=model.score(x_train,y_train)*100
test_score=model.score(x_test, y_test)*100


print("The training score is ",train_score)
print("The test score is ", test_score)

f=open("model.pkl","wb")
dump(model,f)
f.close()

# area=float(input("Enter area"))
# bedroom=float(input("Enter bedroom"))
#
# price=model.predict([[area,bedroom]])
# print("The price is ",price)
