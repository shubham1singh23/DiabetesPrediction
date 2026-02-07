from flask import Flask, request, render_template
from pickle import load

app=Flask(__name__)

@app.route("/",methods=["GET","POST"])
def home():
    if request.method=="POST":
        Sleep_Hours=int(request.form.get("Sleep_Hours"))
        Academic_Performance=int(request.form.get("Academic_Performance"))
        Social_Interactions=int(request.form.get("Social_Interactions"))
        Exercise_Hours=int(request.form.get("Exercise_Hours"))

        f=open("phone.pkl","rb")
        model=load(f)
        result=model.predict([[Sleep_Hours,Academic_Performance,Social_Interactions,Exercise_Hours]])
        f.close()
        return render_template("index.html",result=result)
    else:
        return render_template("index.html")

if __name__=="__main__":
    app.run(debug=True,use_reloader=True)