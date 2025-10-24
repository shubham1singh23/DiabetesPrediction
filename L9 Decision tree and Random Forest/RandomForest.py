import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import matplotlib.pyplot as plt

data=pd.read_csv("Code0_DT.csv")
features=data[["Gender","Occupation"]]
new_features=pd.get_dummies(features)
target=data["Default"]

model=RandomForestClassifier(n_estimators=10)
model.fit(new_features.values,target)




gender=int(input("Enter gender 1.Female 2.Male"))
if gender==1:
    a1=[1,0]
else:
    a1=[0,1]

occ=int(input("Enter the occupation 1.Bussiness 2. Salary"))
if occ==1:
    a2=[1,0]
else:
    a2=[0,1]

a3=[a1+a2]

result=model.predict(a3)
print(result)