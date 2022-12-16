import unittest


class TestLogin(unittest.TestCase):
    def setUp(self):
        print('输入网址.....')

    def tearDown(self):
        print('关闭当前页面....')

    @classmethod
    def setUpClass(cls):
        print('打开浏览器....')

    @classmethod
    def tearDownClass(cls):
        print('关闭浏览器')

    def test_1(self):
        print('输入正确用户名密码，点击登录1')

    def test_2(self):
        print('输入正确用户名密码，点击登录1')
