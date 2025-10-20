import pandas as pd

data=pd.read_csv("Code1_Data_Preprocessing.csv")

# print(data.isnull().sum)
# #drop null
# data=data.dropna()
#
# #fill null with constant
# data=data.fillna({"price":8})
#
# #fill mean with constant
# mean=data["price"].mean()
# data=data.fillna({"price":mean})
# print(data)

#fill median with constant
median=data["price"].median()
data=data.fillna({"price":median})
print(data)

