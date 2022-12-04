import os
from flask import Flask, flash, redirect, render_template, request, session
import time
import json

app = Flask(__name__)

@app.route("/")
def index():
    with open('FileNames.json') as f:
        data = json.load(f)

    ##city = input("Which city?")
    return render_template("index.html", entry=data)