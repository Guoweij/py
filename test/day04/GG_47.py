import json


my_list = [('admin', '123456', '登录成功'), ('root','123456', '登录失败'), ('admin', '123123', '登录失败')]

with open('info4.json','w',encoding='utf-8')as f:
    json.dump(my_list,f,ensure_ascii=False,indent=2)
