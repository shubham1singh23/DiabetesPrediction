import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

data=pd.read_csv('Code2_KNN.csv')
features=data[["A","B"]]

model=KMeans(n_clusters=3,random_state=0,init="k-means++")
clusters=model.fit_predict(features.values)

data["Groups"]=clusters
print(data)

ClusterA=data[data.Groups==0]
ClusterB=data[data.Groups==1]
ClusterC=data[data.Groups==2]

c1=model.cluster_centers_[0]
c2=model.cluster_centers_[1]
c3=model.cluster_centers_[2]

plt.figure(figsize=(11,6))
plt.scatter(ClusterA["A"],ClusterA["B"],color="red",label="Red->Cluster")
plt.scatter(ClusterB["A"],ClusterB["B"],color="blue",label="Blue->Cluster")
plt.scatter(ClusterC["A"],ClusterC["B"],color="green",label="Green->Cluster")
plt.scatter(c1[0],c1[1],marker="x")
plt.scatter(c2[0],c2[1],marker="x")
plt.scatter(c3[0],c3[1],marker="x")
plt.legend()
plt.show()

