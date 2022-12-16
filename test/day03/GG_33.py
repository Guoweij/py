user_list = [
    {"name": "zhangsan", "age": 18},
    {"name": "lisi", "age": 19},
    {"name": "wangwu", "age": 17}
]

user_list.sort(key=lambda x:x['age'],reverse=True)
print(user_list)