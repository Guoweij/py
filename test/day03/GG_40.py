class LoginPage:
    def __init__(self, username, password, code):
        self.username = username
        self.password = password
        self.code = code
        self.bottom = "登录"
    def login(self):
        print(f'输入用户名{self.username}')
        print(f'输入密码{self.password}')
        print(f'输入验证码{self.code}')
        print(f'点击按钮{self.bottom}')

login=LoginPage("abc",123456,888888)
login.login()


