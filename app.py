from flask import url_for, session, Flask, render_template, request, redirect

application = Flask(__name__)
application.secret_key = "asdfghjkl"

ID = "hello"
PW = "world"

@application.route("/")
def home():
    if "userID" in session:
        return render_template("home.html", username = session.get("userID"), login = True)
    else:
        return render_template("home.html",login = False)

@application.route("/login", methods = ["get"])
def login():
    global ID, PW
    __id__ = request.args.get("loginId")
    __password__ = request.args.get("loginPw")

    if ID == __id__ and __password__ == PW:
        session["userID"] = __id__
        return redirect(url_for("home"))
    else:
        return redirect(url_for("home"))

@application.route("/logout")
def logout():
    session.pop("userID")
    return redirect(url_for("home"))

application.run(host ="0.0.0.0")