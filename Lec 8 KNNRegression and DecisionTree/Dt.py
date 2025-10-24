import pandas as pd
from pandas import DataFrame
from sklearn.tree import DecisionTreeClassifier

data=pd.read_csv("Code2_DT.csv")
features=data.drop(["Day","PlayTennis"],axis=1)
target=data["PlayTennis"]
#One hot encoding of categorical data
new_features=pd.get_dummies(features)

model=DecisionTreeClassifier()
model.fit(new_features.values,target)

#Convert to csv file to get the features encoded
# df=DataFrame(new_features)
# df.to_csv("Book1.csv")

result=model.predict([[0,0,1,0,1,0,1,0,0,1]])
print(result)