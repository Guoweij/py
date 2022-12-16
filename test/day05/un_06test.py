import unittest

from day04.tools import add


class TestAdd(unittest.TestCase):
    def test_method1(self):
        if add(1, 2) == 3:
            print("pass")
        else:
            print("failed")

    def test_method2(self):
        if add(10, 20) == 30:
            print("pass")
        else:
            print("failed")

    def test_method3(self):
        if add(2, 3) == 5:
            print("pass")
        else:
            print("failed")
