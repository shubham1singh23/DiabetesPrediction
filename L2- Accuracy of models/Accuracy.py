import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import  LinearRegression

data=pd.read_csv("Code2 - Copy.csv")
data=data.dropna()
features=data[["years"]]
target=data["salary"]

# Split the data into two parts using train_test_split module of sklearn
x_train,x_test,y_train,y_test=train_test_split(features,target,test_size=0.2)

print(x_train,x_test,y_train,y_test)
model=LinearRegression()
# fit using training data
model.fit(x_train,y_train)

# calculate score of training and testing data using model.score
train_score=model.score(x_train,y_train)*100
test_score=model.score(x_test,y_test)*100
print("The training score is",train_score)
print("The test score is",test_score)