import pandas as pd
from sklearn.linear_model import LogisticRegression

data = pd.read_csv("Code4_LoR.csv")
features = data[["hours"]]
target = data["result"]

model = LogisticRegression()
model.fit(features.values,target)

temp = float(input("please enter hours: "))
result = model.predict([[temp]])
print("The result is ",result)

















