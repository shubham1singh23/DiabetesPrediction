from string import punctuation

import pandas as pd
from nltk.corpus import stopwords
from sklearn.linear_model import LinearRegression
from nltk import word_tokenize
from sklearn.feature_extraction.text import CountVectorizer

data=pd.read_csv("Code6.csv")

def clean_function(text):
    text=text.lower()
    text=text.replace("'","")
    text=word_tokenize(text)
    text=[x for x in text if x not in punctuation]
    text=[x for x in text if x not in stopwords.words("english")]
    text=",".join(text)
    return text

data["clean_info"]=data["info"].apply(clean_function)
cv=CountVectorizer()
vector=cv.fit_transform(data["clean_info"])
print(vector)

features=pd.DataFrame(vector.toarray(),columns=cv.get_feature_names_out())
print(features)
