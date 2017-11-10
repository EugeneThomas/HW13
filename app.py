# Eugene Thomas
# SoftDev1 pd7
# HW13 -- A RESTful Journey Skyward
# 2017-11-08


from flask import Flask, request, render_template, session, redirect, url_for, flash
import os
import urllib2, json

app = Flask(__name__) #create instance of class
app.secret_key = os.urandom(32)

### The Root Route:

@app.route('/')
def hello():
    data = urllib2.urlopen("https://api.nasa.gov/planetary/apod?api_key=2xSMrhjPmUbRcvpmuie0c1j1cSGdivcHZcU0uPE0")
    string = data.read()
    d = json.loads(string)
    img = d["url"]
    title = d["title"]
    explanation = d["explanation"]
    date = d["date"]
    copyright = d["copyright"]
    return render_template("nasa.html", image = img, title = title, explanation = explanation, date = date, copyright = copyright)


if __name__=="__main__":
    app.debug = True
    app.run()
