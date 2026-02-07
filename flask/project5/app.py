from flask import *
import sqlite3
app=Flask(__name__)

@app.route("/success")
def success():
    return render_template("success.html")

@app.route("/edit/<int:emp_id>", methods=["GET","POST"])
def edit(emp_id):
    if request.method=="POST":
        name=request.form.get("name")
        salary=int(request.form.get("salary"))
        con = sqlite3.connect("emp.db")
        cursor=con.cursor()
        sql_command=""" UPDATE  employees SET name=?, salary=? WHERE emp_id=?"""
        cursor.execute(sql_command,(name,salary,emp_id))
        con.commit()
        con.close()
        return redirect(url_for("view"))
    else:
         con = sqlite3.connect("emp.db")
         cursor=con.cursor()
         sql_command=""" SELECT * FROM employees WHERE emp_id=?"""
         cursor.execute(sql_command,(emp_id,))
         emp=cursor.fetchone()
         con.commit()
         con.close()
         return render_template("edit.html",emp=emp)


@app.route("/delete/<int:emp_id>")
def delete(emp_id):
    con = sqlite3.connect("emp.db")
    cursor=con.cursor()
    sql_command=""" DELETE FROM employees WHERE emp_id=?"""
    cursor.execute(sql_command,(emp_id,))
    con.commit()
    con.close()
    return redirect(url_for("view"))

@app.route("/employees")
def view():
    con = sqlite3.connect("emp.db")
    cursor=con.cursor()
    sql_command=""" SELECT * FROM employees"""
    cursor.execute(sql_command)
    data=cursor.fetchall()
    con.close()
    return render_template("list.html",data=data)

@app.route("/", methods=["GET","POST"])
def home():
    if request.method=="POST":
        emp_id =int(request.form.get("emp_id"))
        name=request.form.get("name")
        salary=int(request.form.get("salary"))

        con=None
        try:
            con= sqlite3.connect("emp.db")
            cursor=con.cursor()
            sql_command=""" INSERT INTO employees VALUES (?,?,?)"""
            cursor.execute(sql_command,(emp_id,name,salary))
            con.commit()
            return redirect(url_for("success"))
        except Exception as e:
            msg="ERROR" +str(e)
            return render_template("home.html",msg=msg)
        finally:
            con.close()
    else:
        return render_template("home.html")

if __name__ =="__main__":
    app.run(debug=True,use_reloader=True)