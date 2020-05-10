import http.client
import json
import re

def get_ids(history_file, id_list_file):
    ids=[]
    with open(history_file, 'r') as read_file:
        data = json.load(read_file)
    for history in data:
        url = history['url']
        start = re.search('home/', url)
        end = re.search('downPayment', url)
        if start and end:
            start_pos = start.end()
            end_pos = end.start()-1
            house_id = url[start_pos:end_pos]
            ids.append(int(house_id))
    with open(id_list_file, 'w+') as json_file:
        json.dump(list(set(ids)),json_file)

def get_response(id_list_file, output_file):

    with open(id_list_file, 'r') as read_file:
        ids = json.load(read_file)
    with open(output_file,'r') as json_file:
        res = json.load(json_file)

    conn = http.client.HTTPSConnection("api.mashvisor.com")
    key = '403f3c73-8dba-4e9c-9bcc-6c92ab85b37a'
    headers ={'x-api-key': key}
    payload = "{}"

    #index = ids.index(2417529)
    for id in ids:
        print(id)
        params = f'/v1.1/client/property?id={id}&state=TX'
        conn.request("GET", params, payload, headers=headers)
        r1 = conn.getresponse()
        data = r1.read()
        data_str = data.decode('utf8').replace("'", '"')
        try:
            data_json = json.loads(data_str)
            res.append(data_json)
            with open(output_file, 'w+') as f:
                json.dump(res, f)
        except Exception:
            continue
    conn.close()

def read_data():
    with open("property_info.json", "r") as f:
        data = json.load(f)
        print(type(data))
        print(len(data))

history_file = 'history.json'
id_list_file = 'id_list.json'
output_file = 'property_info.json'

#get_ids(history_file, id_list_file)
get_response(id_list_file, output_file)
