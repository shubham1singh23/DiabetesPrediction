from flask import *

app=Flask(__name__)

@app.route("/",methods=['GET','POST'])
def home():
    if request.method=='POST':
        msg= "Welcome "+request.form.get("name")
        return render_template("home.html",msg=msg)
    else:
        return render_template("home.html")


if __name__=="__main__" :
    app.run(use_reloader=True,debug=True)