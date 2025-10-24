import pandas as pd
from sklearn.ensemble import RandomForestClassifier

data=pd.read_csv("Code1_RF.csv")
features=data[["Weather","Energetic"]]
target=data["Running"]

new_features=pd.get_dummies(features)

model=RandomForestClassifier()
model.fit(new_features.values,target)

weather=int(input("Enter weather 1.Rainy 2. sunny"))
if weather==1:
    a1=[1,0]
else:
    a1=[0,1]

energetic=int(input("Enter weather 1.No 2. Yes"))
if energetic==1:
    a2=[1,0]
else:
    a2=[0,1]

a3=[a1+a2]
result=model.predict(a3)
print(result)