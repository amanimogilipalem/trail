#convert .txt file in .json
import json
with open("text.txt", "r") as fin:
    content = json.load(fin)
with open("textJson.txt", "w") as fout:
    json.dump(content, fout)