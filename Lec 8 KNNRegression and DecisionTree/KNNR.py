import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from sklearn.neighbors import KNeighborsRegressor

data=pd.read_csv("Code1_KNN_R.csv")
features=data[["HEIGHT","AGE"]]
target=data["WEIGHT"]

mms=MinMaxScaler()
scaled_features=mms.fit_transform(features.values)

k=int(len(data)**0.5)
if k%2==0:
    k=k+1
model=KNeighborsRegressor(n_neighbors=k)
model.fit(scaled_features,target)

height=float(input("Enter height"))
age=int(input("Enter age"))

a1=[[height,age]]
scaled_a1=mms.transform(a1)

result=model.predict(scaled_a1)
print(result)
