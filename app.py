from flask import Flask, render_template, request, redirect, url_for
import mysql.connector
from datetime import date, datetime

app = Flask(__name__)
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",       
    database="login_app"
)
cursor = db.cursor()

@app.route("/", methods=["GET", "POST"])
def login_page():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        cursor.execute("SELECT * FROM users WHERE username=%s AND password=%s", (username, password))
        user = cursor.fetchone()
        if user:
            return redirect(url_for("calculator_page"))
        else:
            error = "Invalid username or password."
            return render_template("login.html", error=error)
    return render_template("login.html", error=None)

@app.route("/signup", methods=["GET", "POST"])
def signup_page():
    if request.method == "POST":
        username = request.form.get("username")
        email = request.form.get("email")
        password = request.form.get("password")
        cursor.execute("INSERT INTO users (username, email, password) VALUES (%s, %s, %s)", (username, email, password))
        db.commit()
        return redirect(url_for("login_page"))
    return render_template("signup.html")

@app.route("/calculator", methods=["GET", "POST"])
def calculator_page():
    days_lived = None
    if request.method == "POST":
        dob = request.form.get("dob")
        if dob:
            dob_date = datetime.strptime(dob, "%Y-%m-%d").date()
            today = date.today()
            days_lived = (today - dob_date).days
    return render_template("calculator.html", days_lived=days_lived)

if __name__ == "__main__":
    app.run(debug=True, port=5000)