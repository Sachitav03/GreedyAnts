import requests
import urllib.request
#import scrapeTest
from flask import Flask, render_template, request, url_for

app = Flask(__name__, static_url_path='/static')

@app.route("/", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        ingredients = request.form["ingredients"]
        print(ingredients)
    else:
        return render_template("login.html")
        print(ingredients)



{   }
if __name__ == "__main__":
    app.run()
