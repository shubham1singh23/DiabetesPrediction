import pandas as pd
import matplotlib.pyplot as plt

data=pd.read_csv("Code2 - Copy.csv")

plt.figure(figsize=(10,5))
plt.scatter(data["years"],data["salary"])
plt.title("Salary vs Years")
plt.xlabel("Years")
plt.ylabel("Salary")

plt.show()