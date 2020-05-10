import json

res = []

with open("property_info.json", "r") as f:
    data = json.load(f)

for record in data:
    if record['status'] != 'error':
        res.append(record)

with open("property_update.json",'w+') as write_file:
    json.dump(res, write_file)

    
