import json

def read_data():
    with open('info3.json', encoding='utf-8') as  f:
        data = json.load(f)
        new_list = []
        for i in data:
            new_list.append((i.get("username"), i.get("password"), i.get("expect")))

        return new_list
