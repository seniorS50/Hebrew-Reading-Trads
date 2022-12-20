from flask import Flask, render_template, request
from helpers import search_entries, get_text_HULTP
import json

app = Flask(__name__)

# Pre-load dictionary of files from JSON
with open('filenames3.json') as f:
    entries = json.load(f)

# Pre-load dictionary of city locations from JSON
with open('static/city_locs.json') as f:
    cities = json.load(f)

@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/")
def index():
    return render_template("index.html", entries = json.dumps(entries), cities = json.dumps(cities))

@app.route("/listen", methods = ['GET'])
def listen():
    # Read in the get request which has an HULTP number
    HULTP = int(request.args["HULTP"])
    text = get_text_HULTP(HULTP)
    # Get the recording that matches 
    entry = {}
    for item in entries:
        if str(item["HULTP"]) == str(HULTP):
            entry = item
            break
    return render_template("listen.html", entry=entry, text=text)

@app.route("/search", methods = ['GET'])
def search():
    results = search_entries(request.args["q"])
    if request.args:
        return render_template("index.html", entries = json.dumps(results['entries']), cities = json.dumps(results['cities']))
    else:
        return render_template("index.html", entry=[], cities = json.dumps(cities))