import unittest
import requests
from lib.db import get_conn,query_db,change_db

NEW_USER = "孙佩芬"
# 编写一个测试类，以Test开头，继承unittest.TestCase


class TestReg(unittest.TestCase):
    # 编写具体的测试用例方法，以test_开头
    def test_reg_normal(self):
        # 环境检查及数据准备
        conn = get_conn()
        result = query_db(conn,"select id from user where name ='{}'".format(NEW_USER))
        if result:
            change_db(conn, "delete from  `user` where name = '{}'".format(NEW_USER))


        # 组装和发送请求
        url = "http://115.28.108.130:5000/api/user/reg/"
        data = {"name": NEW_USER, "password": "0101"}
        res = requests.post(url=url,json=data)
        res_dict = res.json()
        print(res.json())
        # 断言,传两个参数，assert代表期望结果，Equal代表实际结果
        self.assertEqual("100000",res_dict["code"])
        self.assertEqual("成功", res_dict["msg"])
        self.assertEqual("SHM9", res_dict["data"]["name"])

    def test_reg_exist_user(self):
        url = "http://115.28.108.130:5000/api/user/reg/"
        data = {"name": "SHM2", "password": "0101"}
        res = requests.post(url=url,json=data)
        res_dict = res.json()
        self.assertEqual("100001",res_dict["code"])
        self.assertEqual("失败，用户已存在", res_dict["msg"])
        self.assertEqual("SHM2", res_dict["data"]["name"])


if __name__ == "__main__":
    pass

