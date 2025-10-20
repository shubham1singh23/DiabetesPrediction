import pandas as pd
from sklearn.linear_model import LogisticRegression

data = pd.read_csv("Code4_LoR.csv")
features = data[["hours"]]
target = data["result"]

model = LogisticRegression()
model.fit(features.values,target)

m = model.coef_
c = model.intercept_

temp = float(input("please enter hours: "))
result = 1 / (1+(2.71 ** (-1*(c+m*temp))))

if result > 0.5:
    print("Pass")
else:
    print("Fail")

















