import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
from sklearn.preprocessing import PolynomialFeatures

data =pd.read_csv("Code3_PR.csv")

features=data[["level"]]
target=data["salary"]
pf=PolynomialFeatures(degree=4)
poly_features=pf.fit_transform(features.values)

model=LinearRegression()
model.fit(poly_features,target)

plt.figure(figsize=(10,5))
plt.scatter(data["level"],data["salary"])
plt.plot(data["level"],model.predict(poly_features),color="purple")
plt.show()

level=int(input("Enter level"))
a1=[[level]]
poly_a1=pf.transform(a1)
result=model.predict(poly_a1)
print(result)