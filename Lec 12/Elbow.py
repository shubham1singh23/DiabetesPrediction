import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

data=pd.read_csv("Code_0_KM.csv")
features=data[["Annual_Income","Spending_Score"]]

index=[]
inertia=[]

for i in range(1,9):
    model=KMeans(n_clusters=i,init="k-means++")
    model.fit(features.values)
    index.append(i)
    inertia.append(model.inertia_)

plt.figure(figsize=(10,5))
plt.plot(index,inertia,color="blue",marker="o",markersize=20,markerfacecolor="red")
plt.show()