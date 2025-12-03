import pandas as pd
from sklearn.cluster import  KMeans

data=pd.read_csv('Code1_KNN.csv')
features=data[["X","Y"]]

model=KMeans(n_clusters=2,random_state=0,init="k-means++")
clusters=model.fit(features.values)

data["Groups"]=clusters
print(data)

x=float(input("Enter x"))
y=float(input("Enter y"))

result=model.predict([[x,y]])
print(result)