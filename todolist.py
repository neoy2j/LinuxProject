from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

todolist = Flask(__name__)
USER_DATA = {
    "testuser": "1234"
}

USER_INFO = {}

@todolist.route('/')
def defaultpage():
    return render_template("default.html")

@todolist.route('/login', methods=["GET", "POST"])
def loginpage():
    if request.method == "POST":
        user_id = request.form.get("id")
        user_pw = request.form.get("pw")

        if user_id in USER_INFO and USER_INFO[user_id] == user_pw:
            return render_template("loginsuccess.html")
        else:
            return render_template("loginfail.html")
    
    return render_template("login.html") 

@todolist.route('/main')
def mainpage():
    return render_template("main.html")

@todolist.route('/join', methods=["GET","POST"])
def join():
    if request.method == "POST":
        user_id = request.form.get("id")
        user_pw = request.form.get("pw")
        USER_INFO[user_id] = user_pw
        print(user_id,USER_INFO[user_id])

        return redirect(url_for("loginpage"))
    
    return render_template("join.html")

@todolist.route('/taskmain')
def taskmain():
    return render_template("taskmain.html")

if __name__ == '__main__':
    todolist.run(host='127.0.0.1', port=5500)
