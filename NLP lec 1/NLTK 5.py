from string import punctuation

import pandas as pd
from nltk.corpus import stopwords
from sklearn.linear_model import LinearRegression
from nltk import word_tokenize
data=pd.read_csv("Code5.csv")

target=data["price"]
def clean_function(text):
    text=text.lower()
    text=word_tokenize(text)
    text=[x for x in text if x not in ["area","bedrooms"]]
    text=[x for x in text if x not in punctuation]
    text=[x for x in text if x not in stopwords.words("english")]
    text=",".join(text)
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