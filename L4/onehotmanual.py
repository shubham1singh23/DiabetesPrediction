import pandas as pd
from sklearn.linear_model import LinearRegression

data = pd.read_csv('Code2_OneHot.csv')

features = data[['state', 'city', 'area']]
target = data['price']

new_features = pd.get_dummies(features)

# print(features, new_features)

model = LinearRegression()
model.fit(new_features, target)

area_input = float(input("Enter the area"))

state_input = int(input("Enter the state \n 1- Guj \n 2-Mah"))
if state_input == 1:
    city_input = int(input("Enter the city \n 1-Ahmedabad \n 2-Surat"))
    if city_input == 1:
        price = model.predict([[area_input, 1, 0, 1, 0, 0, 0]])
    elif city_input == 2:
        price = model.predict([[area_input, 1, 0, 0, 0, 0, 1]])
    else:
        print("Invalid city")

    print("The price is", price)

elif state_input == 2:
    city_input = int(input("Enter the city \n 1-Mumbai \n 2-Pune"))
    if city_input == 1:
        price = model.predict([[area_input, 0, 1, 0, 1, 0, 0]])
    elif city_input == 2:
        price = model.predict([[area_input, 0, 1, 0, 0, 1, 0]])
    else:
        print("Invalid city")


else:
    print("Invalid city")

print("The price is", price)