import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

data=pd.read_csv("Code2_KNN.csv")
features=data[["A","B"]]

model=KMeans(n_clusters=3,random_state=0,init="k-means++")
clusters=model.fit_predict(features.values)

data["Group"]=clusters

C1=data[data.Group==0]
C2=data[data.Group==1]
C3=data[data.Group==2]

plt.figure(figsize=(10,5))

plt.scatter(C1["A"],C1["B"],color="red")
plt.scatter(C2["A"],C2["B"],color="yellow")
plt.scatter(C3["A"],C3["B"],color="blue")
plt.show()




