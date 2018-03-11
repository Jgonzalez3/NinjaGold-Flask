# pylint: disable=print-statement

from flask import Flask, render_template, request, redirect, session
import random, datetime, time #use date and time format (Y/m/d I:M p)
app = Flask(__name__)
app.secret_key = "Secret"
log = []
restartlog = []
@app.route("/")
def home():
    return render_template("home.html")

@app.route("/process_money", methods = ["POST"])
def process_money():
    session["log"] = log
    loglength = len(log)
    session["loglength"]= loglength
    print type(session["loglength"])
    print session["log"]
    print session["loglength"]
    building = request.form["building"]
    if building == "farm":
        timestamp = datetime.datetime.now().strftime("(%Y/%m/%d %I:%M %p)")
        earnings = random.randrange(10, 21)
        session["earningsfarm"] = earnings
        gold = earnings
        session["gold"] += gold
        session["timestampfarm"] = timestamp
        ###
        x = "Earned {} golds! from the farm ".format(session['earningsfarm']) + str(timestamp)
        session['log'].append(x)
        ##
        print timestamp
        print "farm earnings", earnings
        print "total gold", session["gold"]
        print "gold", gold
        return redirect("/")
    if building == "cave":
        timestamp = datetime.datetime.now().strftime("(%Y/%m/%d %I:%M %p)")
        earnings = random.randrange(5, 11)
        session["earningscave"] = earnings
        gold = earnings
        session["gold"] += gold
        session["timestampcave"] = timestamp
        ##
        x = "Earned {} golds! from the cave ".format(session['earningscave']) + str(timestamp)
        log.append(x)
        ##
        print timestamp
        print "cave earnings", earnings
        print "total gold", session["gold"]
        print "gold", gold
        return redirect("/")
    if building == "house":
        timestamp = datetime.datetime.now().strftime("(%Y/%m/%d %I:%M %p)")
        earnings = random.randrange(2, 5)
        session["earningshouse"] = earnings
        gold = earnings
        session["gold"] += gold
        session["timestamphouse"] = timestamp
        ##
        x = "Earned {} golds! from the house ".format(session['earningshouse']) + str(timestamp)
        log.append(x)
        ##
        print "house earnings", earnings
        print "total gold", session["gold"]
        print "gold", gold
        return redirect("/")
    if building == "casino":
        timestamp = datetime.datetime.now().strftime("(%Y/%m/%d %I:%M %p)")
        session["timestampcasino"] = timestamp
        chance = random.randrange(0, 51)
        print "chance", chance
        if chance == 50:
            earnings = random.randrange(0, 51)
            session["earningscasino"] = earnings
            gold = earnings
            session["gold"] += gold
            ##
            x = "Earned {} golds! from the casino ".format(session['earningscasino']) + str(timestamp)
            session["log"].append(x)
            ##
            print "casino earnings", earnings
            print "total gold", session["gold"]
            print "gold", gold
            return redirect("/")
        else:
            gamble = random.randrange(0, 51)
            session["gamblecasino"] = gamble
            gold = gamble
            ##
            y = "Entered a casino and lost {} golds... Ouch. ".format(session['gamblecasino']) + str(timestamp)
            log.append(y)
            ##
            if gold > session["gold"]:
                session["gold"] = 0
                return redirect("/")
            else:
                session["gold"] -= gold
                print "casino gamble", gamble
                print "total gold", session["gold"]
                print "gold", gold
                return redirect("/")
    return redirect("/")

@app.route("/restart", methods = ["POST"])
def restart():
    session["gold"] = 0
    ## find a way to remove the logs completely
    session["loglength"] = 0
    log = restartlog
    session["log"] = restartlog
    print log
    print session["loglength"]
    return redirect("/")

app.run(debug=True)