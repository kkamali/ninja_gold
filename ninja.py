from flask import Flask, session, render_template, request, redirect
import random
import datetime

app = Flask(__name__)
app.secret_key = 'ThisIsSecret'

@app.route("/")
def start():
    if ("gold" in session):
        pass
    else:
        session["gold"] = 0
    if ("activities" in session):
        pass
    else:
        session["activities"] = ""
    return render_template("index.html", gold=session["gold"], activity=session["activities"])

@app.route("/process_money", methods=["POST"])
def process():
    if (request.form['building'] == "farm"):
        toAdd = random.randrange(10,21)
        session["gold"] += toAdd
        activityAdd = "Earned " + str(toAdd) + " gold at the farm! (" + str(datetime.datetime.now()) + ")\n"
        print activityAdd
        session["activities"] += activityAdd
    elif (request.form['building'] == "cave"):
        toAdd = random.randrange(5,11)
        session["gold"] += toAdd
        activityAdd = "Earned " + str(toAdd) + " gold at the cave! (" + str(datetime.datetime.now()) + ")\n"
        print activityAdd
        session["activities"] += activityAdd
    elif (request.form['building'] == "house"):
        toAdd = random.randrange(2,6)
        session["gold"] += toAdd
        activityAdd = "Earned " + str(toAdd) + " gold at the house! (" + str(datetime.datetime.now()) + ")\n"
        print activityAdd
        session["activities"] += activityAdd
    else:
        toAdd = random.randrange(-50,51)
        session["gold"] += toAdd
        if (toAdd < 0):
            activityAdd = "Lost " + str(abs(toAdd)) + " gold at the casino! (" + str(datetime.datetime.now()) + ")\n"
        else:
            activityAdd = "Earned " + str(toAdd) + " gold at the casino! (" + str(datetime.datetime.now()) + ")\n"
        print activityAdd
        session["activities"] += activityAdd
    return redirect("/")

@app.route("/reset", methods=["POST"])
def reset():
    session["gold"] = 0
    session["activities"] = ""
    return redirect("/")

app.run(debug=True)
