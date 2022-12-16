def login(username, paswword):
    if username == 'admin' and paswword == '123456':
        return '登录成功'
    else:
        return '登录失败'
