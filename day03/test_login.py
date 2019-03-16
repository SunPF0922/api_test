import unittest
import requests

class Test_login(unittest.TestCase):

    def test_login_normal(self):
        url = "http://115.28.108.130:5000/api/user/login/"
        data = {"name": "SHM", "password": "0101"}
        res = requests.get(url=url, params=data)
        # print(res.text)
        self.assertEqual("<h1>登录成功</h1>",res.text)
        self.assertIn("登录成功",res.text)

