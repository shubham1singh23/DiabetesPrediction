import pandas as pd
from sklearn.neighbors  import KNeighborsClassifier
from sklearn.preprocessing import MinMaxScaler

data=pd.read_csv("Code2_KNN2.csv")

features=data[["Weight","Height"]]
target=data["Class"]

k=int(len(data))
if k%2==0:
    k=k+1;
    


mms = MinMaxScaler()
scaled_features = mms.fit_transform(features.values)

model=KNeighborsClassifier(n_neighbors=k)
model.fit(scaled_features,target)

h=int(input("Enter the height"))
w=int(input("Enter the weight"))

a1=[[h,w]]
scaled_a1=mms.transform(a1)

result=model.predict(scaled_a1)
print(result)