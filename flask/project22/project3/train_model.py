import pandas as pd
from sklearn.linear_model import LinearRegression
from pickle import dump

data=pd.read_csv("phone_data.csv")

features=data[["Sleep_Hours","Academic_Performance","Social_Interactions","Exercise_Hours"]]
target=data["Addiction_Level"]

model=LinearRegression()
model.fit(features.values,target)

f=open("phone.pkl","wb")
dump(model,f)
f.close()
