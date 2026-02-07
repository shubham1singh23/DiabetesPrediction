from flask import *
import sqlite3
app=Flask(__name__)

@app.route("/",methods=['GET','POST'])
def home():
    if request.method=='POST':
        name=request.form.get("name")
        phone=int(request.form.get("phone"))
        query=request.form.get("query") 
        con=None
        try:
           con=sqlite3.connect("doubts.db")
           cursor=con.cursor()
           sql_command="""
           insert into student values(?,?,?)
           """
           cursor.execute(sql_command,(name,phone,query))
           con.commit()
           return render_template("home.html",msg="Success")
        except Exception as e:
            msg="Error" + str(e)
            return render_template("home.html",msg=msg)
    else:
        return render_template("home.html")


if __name__=="__main__" :
    app.run(use_reloader=True,debug=True)