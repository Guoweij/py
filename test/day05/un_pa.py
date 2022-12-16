import unittest
from parameterized import parameterized

from day05.tools import login

data = [
    ('admin', '123456', '登录成功'),
    ('root', '123456', '登录成功'),
    ('admin', '123123', '登录失败'),
]


class TestLogin(unittest.TestCase):
    @parameterized.expand(data)
    def test_login(self, username, password, expect):  # 数据和参数要保持一致  是通过位置传参的
        self.assertEqual(expect, login(username, password))
