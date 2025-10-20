import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import MinMaxScaler


data=pd.read_csv("Code3_LC.csv")
features=data.drop(["LUNG_CANCER"],axis=1)
features=pd.get_dummies(features)
target=data["LUNG_CANCER"]

mms=MinMaxScaler()
features=mms.fit_transform(features.values)

k=int(len(data))
if k%2==0:
    k=k+1

model=KNeighborsClassifier()
model.fit(features,target)

# tupple=[[69,1,2,2,1,1,2,1,2,2,2,2,2,2,0,1]]
# scaled_tupple=mms.transform(tupple)

df=pd.DataFrame(features)
df.to_csv("Scaled.csv")

tupple=[[0.8030303030303032,1.0,0.0,0.0,0.0,1.0,1.0,1.0,0.0,0.0,0.0,1.0,1.0,1.0,0.0,1.0]]
result=model.predict(tupple)
print(result)