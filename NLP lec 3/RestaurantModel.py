import pandas as pd
from pandas.core.common import random_state

data=pd.read_csv("rest.tsv",sep="\t")
print(data)
#%%


from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

cv=CountVectorizer(ngram_range=(1,3))
vector=cv.fit_transform(data["Review"])

features=pd.DataFrame(vector.toarray(),columns=cv.get_feature_names_out())
target=data["Liked"]

x_train,x_test,y_train,y_test=train_test_split(features.values,target,random_state=2)

model=MultinomialNB()
model.fit(x_train,y_train)

cr=classification_report(y_test,model.predict(x_test))
print(cr)
#%%
from pickle import dump

f=open("RestModel.pkl","wb")
dump(model,f)
f.close()

f=open("Countvector3.pkl","wb")
dump(cv,f)
f.close()

print("done")