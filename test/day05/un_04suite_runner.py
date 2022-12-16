# 1. 导包(unittest)
# 2. 实例化(创建对象)套件对象
# 3. 使⽤套件对象添加⽤例⽅法
# 4. 实例化运⾏对象
# 5. 使⽤运⾏对象去执⾏套件对象

import unittest

from day05.un_02 import TestDemo1
from day05.un_03 import TestDemo2

suite = unittest.TestSuite()

suite.addTest(TestDemo1('test_method1'))
suite.addTest(TestDemo1('test_method2'))
suite.addTest(TestDemo2('test_method1'))
suite.addTest(TestDemo2('test_method2'))

runner = unittest.TextTestRunner()

runner.run(suite)
