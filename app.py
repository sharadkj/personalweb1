from flask import Flask
from flask import render_template
from datetime import date

app = Flask(__name__)

def todays_date():
    today = date.today()
    str_date = today.strftime("%B %d %Y")
    return("Today's date is " + str_date)

@app.route("/")
def hello_world():
    today = todays_date()
    return(render_template("index.html", the_date = today))

@app.route("/about")
def about_me():
    return(render_template("about_me.html"))
