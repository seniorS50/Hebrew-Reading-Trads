import json
import os

with open('FileNames.json') as f:
    data = json.load(f)


for datum in data:
    if not os.path.isfile('static/mp3/' + datum["File"] + '.mp3'):
        print(f'static/mp3/' + datum["File"] + '.mp3 does not exist!')
