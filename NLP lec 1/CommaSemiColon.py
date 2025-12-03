import pandas as pd
from sklearn.linear_model import LinearRegression

data=pd.read_csv("Code2.csv")

target=data["price"]
def clean_function(text):
    text=text.replace(";","")
    return text

data["clean_info"]=data["info"].apply(clean_function)
data[["area","bedrooms"]]=data["clean_info"].str.split(",",expand=True)
features=data[["area","bedrooms"]]

model=LinearRegression()
model.fit(features.values,target)

area=float(input("Enter the area : "))
bedrooms=int(input("Enter the bedrooms : "))

result=model.predict([[area,bedrooms]])
print(result)