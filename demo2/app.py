from flask import Flask, url_for


app = Flask(__name__)


@app.route("/")
def hello():
    my_url = url_for(99)
    return "Here's a URL: {}".format(my_url)


@app.route("/pizza")
def ninety_nine():
    return "pizza is good"
