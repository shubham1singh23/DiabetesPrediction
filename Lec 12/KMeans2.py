import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

data=pd.read_csv("Code_0_KM.csv")
features=data[["Annual_Income","Spending_Score"]]

model=KMeans(n_clusters=5, init="k-means++",random_state=0)
clusters=model.fit_predict(features.values)

data["Groups"]=clusters

C0=data[data.Groups==0]
C1=data[data.Groups==1]
C2=data[data.Groups==2]
C3=data[data.Groups==3]
C4=data[data.Groups==4]

plt.figure(figsize=(10,5))
plt.scatter(C0["Annual_Income"],C0["Spending_Score"],color="red")
plt.scatter(C1["Annual_Income"],C1["Spending_Score"],color="blue")
plt.scatter(C2["Annual_Income"],C2["Spending_Score"],color="pink")
plt.scatter(C3["Annual_Income"],C3["Spending_Score"],color="yellow")
plt.scatter(C4["Annual_Income"],C4["Spending_Score"],color="green")

plt.show()

income=int(input("Enter income"))
Score=int(input("Enter Score"))

result=model.predict([[income,Score]])

if result==0:
    print("MI MS")
elif result==1:
    print("HIS")
elif result==2:
    print("HI LS")
elif result==3:
    print("LI LS")
else:
    print("LI HS")