import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer


f1=input("Enter name of first file")+str(".txt")
f2=input("Enter name of second file")+str(".txt")

f1=open(f1,"r")
f2=open(f2,"r")

s1=f1.read()
s2=f2.read()

f1.close()
f2.close()



cv=CountVectorizer()
vectors=cv.fit_transform([s1,s2])

cs=cosine_similarity(vectors[0],vectors[1])
print(cs*100)