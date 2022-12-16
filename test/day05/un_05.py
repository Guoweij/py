import unittest

# 2. 实例化(创建对象)套件对象,
from day05.un_02 import TestDemo1
from day05.un_03 import TestDemo2

suite = unittest.TestSuite()
# 3. 使⽤套件对象添加⽤例⽅法
# ⽅式⼀, 套件对象.addTest(测试类名('⽅法名')) #
# 建议测试类名和⽅法名直接去复制,不要⼿写
# 方式二
# 套件对象.addTest(unittest.makeSuite(测试类名))
suite.addTest(unittest.makeSuite(TestDemo1))
suite.addTest(unittest.makeSuite(TestDemo2))
# 4. 实例化运⾏对象
runner = unittest.TextTestRunner()
# 5. 使⽤运⾏对象去执⾏套件对象
# 运⾏对象.run(套件对象)
runner.run(suite)