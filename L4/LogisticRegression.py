import pandas as pd
from sklearn.linear_model import LogisticRegression

data=pd.read_csv("Code4_LoR.csv")

features=data[["hours"]]
target=data["result"]

model=LogisticRegression()
model.fit(features.values,target)

hours=float(input("Enter hours"))
result=model.predict([[hours]])

print("your result is " ,result)
