import pandas as pd
from sklearn.tree import DecisionTreeRegressor,plot_tree
import matplotlib.pyplot as plt

data =pd.read_csv("Code_1_DTR.csv")
features=data[["Position","Level"]]
features=pd.get_dummies(features)
target=data["Salary"]

model=DecisionTreeRegressor(criterion="entropy")
history=model.fit(features.values,target)

hr=float(input("Enter hours : "))
result=model.predict([[hr]])
print(result)

plt.figure(figsize=(11,6))
plot_tree(history,feature_names=["hours"],class_names=["fail","pass"])
plt.fill()
plt.show()