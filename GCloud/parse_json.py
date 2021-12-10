import json

with open("GCloud\Tesco-Customer-Data.json", "r") as tesco_json:
    data = json.load(tesco_json)
print(data)