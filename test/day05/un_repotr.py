import unittest

from HTMLTestRunner import HTMLTestRunner

suite =unittest.defaultTestLoader.discover('.','un_pa.py')
file = 'report2.html'
with open(file,'wb')as f:
    runner = HTMLTestRunner(f, 2, '测试报告', 'Python 3.6.8')
    runner.run(suite)