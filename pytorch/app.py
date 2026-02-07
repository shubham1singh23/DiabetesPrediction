import pandas as pd
from sklearn.preprocessing import StandardScaler
import torch.nn as nn


data=pd.read_csv("data.csv")
features=data[["hours_studied","attendance","sleep_hours","previous_score"]]
target=data["final_score"]

ss=StandardScaler()
scaled_features=ss.fit_transform(features.values)
import torch
tensor_features=torch.tensor(scaled_features,dtype=torch.float32)
tensor_target=torch.tensor(target,dtype=torch.float32).view(-1,1)

model=nn.Linear(4,1)
mse=nn.MSELoss()
optimiser=torch.optim.SGD(model.parameters(),lr=0.01)

for epoch in range(2000):
    y_pred=model(tensor_features)
    loss=mse(y_pred,tensor_target)
    loss.backward()
    optimiser.step()
    optimiser.zero_grad()
    if epoch%100==0:
        print("Loss is",loss)

hrs=float(input("Enter hours : "))
attendance=float(input("Enter attendance "))
sleep=float(input("Enter sleep : "))
prev=float(input("Enter prev :"))

a1=[[hrs,attendance,sleep,prev]]
scaled_a1=ss.transform(a1)
tensor_a1=torch.tensor(scaled_a1,dtype=torch.float32)

result=model(tensor_a1).item()
print(result)