import unittest
from HTMLTestRunner_PY3 import HTMLTestRunner

# 使用unittest默认的加载器遍历发现所有test开头py文件中所有Test类中的test开头方法
# 返回一个包含所有用例的测试集合
suite = unittest.defaultTestLoader.discover("./",pattern="test_case*")
# unittest.TextTestRunner(verbosity=2).run(suite)
# 新建一个用例执行器
# runner = unittest.TextTestRunner(verbosity=2)
# 使用执行器执行测试集合
# runner.run(suite)

f = open("report.html","wb")
runner = HTMLTestRunner(stream=f,title="用例执行结果",description="课堂练习")
runner.run(suite)

f.close()