import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import  classification_report
from sklearn.ensemble import RandomForestClassifier

data=pd.read_csv("../L10 Feature Engineering/Code2_RF.csv", header=None)
data.columns=["buying","maintenance","doors","person","lg_boot","safety","class"]
features=pd.get_dummies(data.drop(["class"],axis=1))
target=data["class"]

x_train,x_test,y_train,y_test=train_test_split(features.values,target)

# model=DecisionTreeClassifier()
model=RandomForestClassifier(n_estimators=10)
model.fit(x_train,y_train)

cr=classification_report(y_test,model.predict(x_test))

# df=pd.DataFrame(features)
# df.to_csv("Book1")

result=model.predict([[0,0,0,1,0,0,0,1,1,0,0,0,1,0,0,0,0,1,0,1,0]])
print(result)
