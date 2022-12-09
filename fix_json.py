import json

with open('FileNames2.json') as f:
    files = json.load(f)
for file in files:
    file['HULTP'] = str(file['HULTP'])
    file['year'] = str(file['year'])

out_file = open("filenames3.json", "w")
  
json.dump(files, out_file, indent = 6)
  
out_file.close()