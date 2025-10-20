from pickle import *
f=open("model.pkl","rb")
model=load(f)
f.close()

area=float(input("Enter area"))
bedroom=float(input("Enter bedroom"))

price=model.predict([[area,bedroom]])
print("The price is ",price)