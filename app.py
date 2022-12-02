import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.security import check_password_hash, generate_password_hash
import time
import json

app = Flask(__name__)

@app.route("/")
def index():
    cities = open('city_locs.json')
    return render_template("index.html", cities=cities)