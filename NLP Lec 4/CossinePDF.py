import fitz
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer


name1=input("Enter name of first file")+str(".pdf")
name2=input("Enter name of second file")+str(".pdf")

f1=fitz.open(name1)
s1=""
s2=""
for page in f1:
    s1=s1+page.get_text()
f2=fitz.open(name2)

for page in f2:
    s2=s2+page.get_text()



cv=CountVectorizer()
vectors=cv.fit_transform([s1,s2])

cs=cosine_similarity(vectors[0],vectors[1])
print(cs*100)