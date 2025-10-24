import pandas as pd
from sklearn.tree import DecisionTreeClassifier

data=pd.read_csv("Code3_DT.csv")
features=data.drop(["LOAN APPROVED"],axis=1)
target=data["LOAN APPROVED"]

new_features=pd.get_dummies(features)

model=DecisionTreeClassifier()
model.fit(new_features.values,target)

df=pd.DataFrame(new_features)
df.to_csv("Onehotfeatures")

result=model.predict([[0,0,1,1,0,0,0,1,0]])
print(result)
