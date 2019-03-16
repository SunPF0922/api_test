import unittest
from test_login2 import TestLogin2,TestReg2

# 新建测试套件（组织用例）
suite = unittest.TestSuite()
# 逐条添加
suite.addTest(TestLogin2("test_login"))
suite.addTest(TestReg2("test_reg"))
# 批量添加
suite.addTest([])
