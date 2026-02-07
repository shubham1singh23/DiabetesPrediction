import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
from pickle import dump
data=pd.read_csv("diabetes.csv")
data=data.drop(["Pregnancies"],axis=1)

features=data.drop(["Outcome"],axis=1)
target=data["Outcome"]

x_train,x_test,y_train,y_test=train_test_split(features.values,target,random_state=82)

model=LogisticRegression(max_iter=1000)
model.fit(x_train,y_train)

cr=classification_report(y_test,model.predict(x_test))
print(cr)

f=open("diab.pkl","wb")
dump(model,f)
f.close()