from sklearn.linear_model import LinearRegression
import pandas as pd

# Load data
data = pd.read_csv("Code2_OneHot.csv")

print(data["state"].unique())
print(data["city"].unique())

# Select features and target
features = data[["state", "city", "area"]]
target = data["price"]

# One-hot encoding
new_features = pd.get_dummies(features)

# Train model
model = LinearRegression()
model.fit(new_features, target)

# === Take input from user ===
area = float(input("Enter the area: "))
state = input("Enter the state: ").strip()
city = input("Enter the city: ").strip()

# Create a zero row with same columns as training data
input_data = {col: 0 for col in new_features.columns}
input_data["area"] = area

# Set the correct one-hot values
state_col = f"state_{state}"
city_col = f"city_{city}"

if state_col in input_data:
    input_data[state_col] = 1
if city_col in input_data:
    input_data[city_col] = 1

# Convert to DataFrame
input_df = pd.DataFrame([input_data])

# Predict price
predicted_price = model.predict(input_df)
print("Predicted Price:", predicted_price)
