import pandas as pd
from sklearn.cluster import KMeans

data=pd.read_csv('Code2_KNN.csv')
features=data[["A","B"]]

model=KMeans(n_clusters=3,random_state=0,init="k-means++")
clusters=model.fit_predict(features.values)

data["Groups"]=clusters
print(data)

a=int(input("Enter a : "))
b=int(input("Enter b : "))

result=model.predict([[a,b]])

if result ==0:
    print("Cluster A")
elif result==1:
    print("Cluster B")
else:
    print("Cluster C")