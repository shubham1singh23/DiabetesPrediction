from flask import Flask, render_template,request
from pickle import load

app=Flask(__name__)

@app.route("/",methods=["GET","POST"])
def home():
    if request.method=="POST":
        glucose=int(request.form.get("glucose"))
        bp=int(request.form.get("bp"))
        skin=int(request.form.get("skin"))
        insulin=int(request.form.get("insulin"))
        bmi=float(request.form.get("bmi"))
        dpf=float(request.form.get("dpf"))
        age=int(request.form.get("age"))

        f=open("diab.pkl","rb")
        model=load(f)
        f.close()
        result=model.predict([[glucose,bp,skin,insulin,bmi,dpf,age]])
        if result==1:
            msg="Diabetic"
        else:
            msg="Non Diabetic"
        return render_template("home.html",msg=msg)
    else:
        return render_template("home.html")


if __name__=="__main__":
    app.run(debug=True,use_reloader=True)