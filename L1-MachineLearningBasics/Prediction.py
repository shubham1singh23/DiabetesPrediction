import pandas as pd
from sklearn.linear_model import LinearRegression

# import the csv file in dataframe
data =pd.read_csv("Code1.csv")

# define the features on which basis the prediction is to be made
features=data[["area"]]

# define the target whose value is to be predicted
target=data["price"]

# create object instance of the model
model=LinearRegression()

# train the data with features and target
# features.value converts the data frame into ndarray of numpy
model.fit(features.values,target)

# input the area of which price is to be predicted
area=float(input("Enter the area: "))

# predict the price by giving feature value
price=model.predict([[area]])

print("The predicted price is ",price)