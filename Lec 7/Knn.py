import pandas as pd
from sklearn.neighbors  import KNeighborsClassifier
from sklearn.preprocessing import MinMaxScaler

data=pd.read_csv("Code1_KNN.csv")

features=data[["Height(cm)","Weight(kg)"]]
target=data["T-Shirt Size"]


#scale the data into similar scale
mms = MinMaxScaler()
#fit data in min max scaler object and also get a scaled data
scaled_features = mms.fit_transform(features.values)


#create model and fit the scaled data
model=KNeighborsClassifier()
model.fit(scaled_features,target)

h=int(input("Enter the height"))
w=int(input("Enter the weight"))

#scale the values to be predicted
a1=[[h,w]]
scaled_a1=mms.transform(a1)

#predict the answer
result=model.predict(scaled_a1)
print(result)