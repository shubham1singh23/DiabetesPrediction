import pandas as pd
import matplotlib.pyplot as plt

# make a dataframe and read from csv
# 2d data array is called dataframe
data=pd.read_csv("Code1.csv")

# Make a series of 1d data to pass to scatter plot
X=data["area"]
Y=data["price"]
# Call the plot function
plt.scatter(X,Y,color='red')

# Give titles and label
plt.title("Powai Real Estate")
plt.xlabel("Area")
plt.ylabel("Price")

# Display the plot on the screen
plt.show()