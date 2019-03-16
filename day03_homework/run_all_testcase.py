import unittest

from HTMLTestRunner_PY3 import HTMLTestRunner

# 新建一个测试套件，遍历根目录下所有test开头文件的test类下的test方法
suite = unittest.defaultTestLoader.discover("./", pattern="test_case*")

f = open("report1.html", "wb")

runner = HTMLTestRunner(stream=f, title="用例执行结果", description="课后作业")
runner.run(suite)

f.close()


