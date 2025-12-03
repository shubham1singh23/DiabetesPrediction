import pandas as pd
from sklearn.cluster import  KMeans
import matplotlib.pyplot as plt

data=pd.read_csv('Code1_KNN.csv')
features=data[["X","Y"]]

model=KMeans(n_clusters=2,random_state=0,init="k-means++")
clusters=model.fit_predict(features.values)

data["Groups"]=clusters
print(data)
Cluster1=data[data.Groups==1]
Cluster2=data[data.Groups==0]

c1=model.cluster_centers_[1]
c0=model.cluster_centers_[0]

plt.figure(figsize=(11,6))
plt.scatter(Cluster1["X"],Cluster1["Y"],color="red",label="Red->Cluster 0")
plt.scatter(Cluster2["X"],Cluster2["Y"],color="blue",label="Red->Cluster 1")
plt.scatter(c1[0],c1[1],marker="x")
plt.scatter(c0[0],c0[1],marker="x")
plt.legend()
plt.show()


