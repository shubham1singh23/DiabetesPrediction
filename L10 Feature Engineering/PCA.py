import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import  classification_report
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

data=pd.read_csv("Code2_RF.csv",header=None)
data.columns=["buying","maintenance","doors","person","lg_boot","safety","class"]
features=pd.get_dummies(data.drop(["class"],axis=1))
target=data["class"]

# scaling to match 0/1 categorical data and numerical data
ss=StandardScaler()
scaled_features=ss.fit_transform(features.values)

# decompose using pca algorithm to given number of components
pca=PCA(n_components=2)
p_features=pca.fit_transform(scaled_features)

# printing the shape of the features
print(features.shape)
print(scaled_features.shape)
print(p_features.shape)

# pass pca features to the train test split
x_train,x_test,y_train,y_test=train_test_split(p_features,target)
model=DecisionTreeClassifier()
model.fit(x_train,y_train)



cr=classification_report(y_test,model.predict(x_test))
print(cr)

