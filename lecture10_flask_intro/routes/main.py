from app import app
from flask import render_template


@app.route("/")
def hello():
    a = "=== Welcome to CURSOR ==="
    return render_template("index.html", variable=a)

@app.route("/add/<x>/<y>")
def adding(x, y):
    a = int(x) + int(y)
    b = str(a)
    return b
