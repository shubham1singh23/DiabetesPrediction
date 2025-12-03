import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import MinMaxScaler

data=pd.read_csv('Code3_KNN.csv')
features=data[["RUNS","WICKETS"]]

mms=MinMaxScaler()
scaled_features=mms.fit_transform(features.values)

model=KMeans(n_clusters=2,random_state=0,init="k-means++")
cluster=model.fit_predict(scaled_features)

data["Groups"]=cluster

runs=int(input("Enter runs : "))
wicket =int(input("Enter wickets"))


a1=[[runs,wicket]]
scaled_a1=mms.transform(a1)

result=model.predict(scaled_a1)
if result==1:
    print("Batsman")
else:
    print("Bowler")