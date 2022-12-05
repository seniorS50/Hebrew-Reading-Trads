import os
from flask import Flask, flash, redirect, render_template, request, session
from helpers import search_entries
import time
import json

app = Flask(__name__)

# Pre-load dictionary of files from JSON
with open('FileNames.json') as f:
    data = json.load(f)

@app.route("/")
def index():

    ##city = input("Which city?")
    return render_template("index.html", entry=data)

@app.route("/search", methods = ['GET'])
def search():
    ## City = input("Which city?")
    if request.args:
        return render_template("index.html",entry=search_entries(request.args["q"]))
    else:
        return render_template("index.html",entry=[])

@app.route('/process', methods=['POST'])
def process_data():
    coords = 