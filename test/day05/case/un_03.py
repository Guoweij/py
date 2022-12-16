# 1. 导包 (unittest)
# 2. ⾃定义测试类
# 3. 在测试类中书写测试⽅法
# 4. 执⾏⽤例
import unittest


class TestDemo2(unittest.TestCase):
    def test_method1(self):
        print("test2-1")

    def test_method2(self):
        print('test2-2')