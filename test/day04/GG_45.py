import json

with open('info.json', encoding='utf-8') as f:
    # buf = f.read()
    # print(buf)
    result = json.load(f)
    print(type(result))  # dict 字典
    print(result.get('name'))
    print(result.get('age'))
    print(result.get('address'))
    print(result.get('address').get('city'))
