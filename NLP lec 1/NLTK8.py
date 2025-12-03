import pandas as pd
from string import punctuation
from nltk.corpus import  stopwords
from nltk import word_tokenize
from pyexpat import features
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

data=pd.read_csv("Code8.csv")

def clean_function(text):
    text=text.lower()
    text=word_tokenize(text)
    text=[x for x in text if x not in punctuation]
    text=[x for x in text if x not in stopwords.words("english")]
    text=",".join(text)
    return text

data["clean_review"]=data["review"].apply(clean_function)
cv=CountVectorizer()
vector=cv.fit_transform(data["clean_review"])

features=pd.DataFrame(vector.toarray(),columns=cv.get_feature_names_out())
print(features)
target=data["result"]

model=MultinomialNB()
model.fit(features.values,target)

review=input("Enter the movie review :")
clean_review=clean_function(review)
vector_review=cv.transform([clean_review])
result=model.predict(vector_review)

print(result)