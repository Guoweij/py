import unittest

from day05.un_06test import TestAdd

suite=unittest.TestSuite()
suite.addTest(unittest.makeSuite(TestAdd))
runner =unittest.TextTestRunner()
runner.run(suite)