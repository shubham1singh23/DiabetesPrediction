import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from pickle import dump

data = pd.read_csv("spam.csv")

import spacy
nlp = spacy.load("en_core_web_lg")

def clean_function(text):
    text = text.lower()
    text = nlp(text)
    text = [t for t in text]
    text = [t for t in text if not t.is_punct]
    text = [t for t in text if not t.is_stop]
    text = [t.lemma_ for t in text]
    text = [str(t) for t in text]
    text = " ".join(text)
    return text


data["clean_review"] = data["review"].apply(clean_function)
tv = TfidfVectorizer()
vector = tv.fit_transform(data["clean_review"])
features = pd.DataFrame(vector.toarray(), columns= tv.get_feature_names_out())
target = data["result"]

model = MultinomialNB()
model.fit(features.values,target)

f = open("model.pkl" , "wb")
dump(model,f)
f.close()

f = open("vector.pkl" , "wb")
dump(tv,f)
f.close()