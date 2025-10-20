import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

data = pd.read_csv("Code4_LoR.csv")
features = data[["hours"]]
target = data["result"]

x_train,x_test,y_train,y_test = train_test_split(features.values,target)
model = LogisticRegression()
model.fit(x_train,y_train)

print(y_test)
print(model.predict(x_test))

temp = accuracy_score(y_test,model.predict(x_test))
print("The accuracy is ",temp*100)




























