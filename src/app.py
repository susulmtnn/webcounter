from flask import Flask, redirect, render_template, request
from counter import Counter
import json

app = Flask(__name__)
cnt = Counter()

@app.route("/")
def index():
    return render_template("index.html", value=cnt.value)

@app.route("/increment", methods=["POST"])
def increment():
    cnt.increase()
    return redirect("/")

@app.route("/reset", methods=["POST"])
def reset():
    cnt.reset()
    return redirect("/")

@app.route("/inputvalue", methods=["POST"])
def inputvalue():
    aseta=request.form.get("aseta")
    cnt.inputvalue(aseta)
    return redirect("/")