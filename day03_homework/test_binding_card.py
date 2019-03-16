import json

import requests

import unittest

from common_params import get_binding_params

from use_DB import change_db,get_conn

from binding_card import binding_card04,binding_card,binding_card02


class TestBindingCard(unittest.TestCase):
    def test_binding_normal(self):
        conn = get_conn()
        change_db(conn, 'UPDATE cardinfo SET cardstatus = "",userId = "" WHERE cardNumber = "0922"')
        data, _ = get_binding_params()
        _, url = get_binding_params()
        res = requests.post(url=url, json=data)
        # print(res.json())
        dict = res.json()
        self.assertEqual(5010, dict["code"])
        self.assertIn("成功", dict["msg"])

    def test_binding_again(self):
        dict = binding_card()
        self.assertEqual(5014, dict["code"])
        self.assertIn("只能绑定两张卡", dict["msg"])
        self.assertFalse(False, dict["success"])

    def test_binding_card03(self):  # 证件类型为空5031
        dict = binding_card04()
        self.assertEqual(5031, dict["code"])

    def test_binding_card04(self):
        conn = get_conn()
        change_db(conn, 'UPDATE cardinfo SET cardstatus = "5012" WHERE cardNumber = "11112"')
        dict = binding_card02()
        self.assertEqual(5012,dict["code"])
        self.assertIn("已经注销", dict["msg"])





