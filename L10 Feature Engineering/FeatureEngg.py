import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import  classification_report
from sklearn.ensemble import RandomForestClassifier
from matplotlib import pyplot as plt

data=pd.read_csv("Code2_RF.csv",header=None)
data.columns=["buying","maintenance","doors","person","lg_boot","safety","class"]
data=data.drop(["doors","lg_boot"],axis=1)
features=pd.get_dummies(data.drop(["class"],axis=1))
target=data["class"]

x_train,x_test,y_train,y_test=train_test_split(features.values,target)

# model=DecisionTreeClassifier()
model=RandomForestClassifier(n_estimators=10)
model.fit(x_train,y_train)

# do this before dropping to see the importance of the features and then drop accordingly
plt.figure(figsize=(11,6))
X=features.columns
Y=model.feature_importances_
plt.barh(X,Y)
plt.show()

cr=classification_report(y_test,model.predict(x_test))
print(cr)
# df=pd.DataFrame(features)
# df.to_csv("Book1")
#
# result=model.predict([[0,0,0,1,0,0,0,1,1,0,0,0,1,0,0,0,0,1,0,1,0]])
# print(result)
