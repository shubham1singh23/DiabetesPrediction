import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt


data=pd.read_csv("Code1.csv")

features=data[["area"]]
X=data["area"]
Y=data["price"]

model = LinearRegression()
model.fit(data[["area"]],data["price"])

plt.figure(figsize=(10,5))
# plot the actual data
plt.scatter(X,Y,color='red')

# plot the predicted values against the features
plt.plot(X,model.predict(features),color='blue')

plt.title("Powai Real Estate")
plt.xlabel("Area")
plt.ylabel("Price")


plt.show()