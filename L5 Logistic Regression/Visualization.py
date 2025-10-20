import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("Code4_LoR.csv")

plt.figure(figsize=(10,5))
plt.scatter(data["hours"],data["result"])
plt.title("Exam")
plt.xlabel("Hours")
plt.ylabel("Result")
plt.show()