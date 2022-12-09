<<<<<<<< HEAD:app.py
from flask import Flask, render_template, request
from helpers import search_entries, get_text_HULTP
========
import os
from flask import Flask, flash, redirect, render_template, request, session, send_from_directory
from helpers import search_entries, get_hebrew_text_HULTP
import time
>>>>>>>> 5a4855c0034a70ad3c47f80978444d4c8f150995:project/app.py
import json

app = Flask(__name__)

# Pre-load dictionary of files from JSON
with open('FileNames.json') as f:
    data = json.load(f)

@app.route("/")
def index():
    return render_template("index.html", entry=data)

@app.route("/listen", methods = ['GET'])
def listen():
    # Read in the get request which has an HULTP number
    HULTP = int(request.args["HULTP"])
    text = get_text_HULTP(HULTP)
    # Get the recording that matches 
    for datum in data:
        if datum["HULTP"] == HULTP:
            entry = datum
            break
    return render_template("listen.html", entry=entry, text=text)

@app.route("/search", methods = ['GET'])
def search():
    if request.args:
        return render_template("index.html",entry=search_entries(request.args["q"]))
    else:
        return render_template("index.html",entry=[])