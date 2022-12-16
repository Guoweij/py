import unittest

version = 29

class DemoTest(unittest.TestCase):
    @unittest.skip("跳过")
    def test_1(self):
        print("测试1")

    @unittest.skipIf(version > 30, "大于30跳过")
    def test_2(self):
        print("测试2")

    def test_3(self):
        print("测试3")

    def test_4(self):
        print("测试4")
