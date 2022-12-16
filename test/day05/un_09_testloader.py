import unittest

# 2, 实例化加载对象并添加用例
# unittest.TestLoader().discover('用例所在的路径', '用例的代码文件名')
# 用例所在的路径,建议使用相对路径, 用例的代码文件名可以使用 *(任意多个任意字符) 通配符
# suite = unittest.TestLoader().discover('./case', 'un*.py')
# suite = unittest.TestLoader().discover('./case', '*0*.py')
suite = unittest.TestLoader().discover('./case', '*.py')

# runner = unittest.TextTestRunner()
# runner.run(suite)

unittest.TextTestRunner().run(suite)
