import requests

from use_DB import query_db,change_db,get_conn
from common import get_card,del_card
from common_params import get_params
import json

import unittest


NEW_CardId = "0922321321"


class TestAddCard(unittest.TestCase):
    def test_add01(self):
        conn = get_conn()
        """
        result = query_db(conn, "SELECT * FROM cardinfo WHERE cardNumber = '{}'". format(NEW_CardId))
        print(result)
        if result:
            change_db(conn, "DELETE FROM cardinfo WHERE cardNumber = '{}'".format(NEW_CardId))
            """
        if get_card(conn, NEW_CardId):
            del_card(conn, NEW_CardId)
        data = {"dataSourceId": "endq", "methodId": "00A", "CardInfo": {
            "cardNumber": NEW_CardId
        }}
        url = "http://115.28.108.130:8080/gasStation/process"
        # data["CardInfo"]["cardNumber"] = NEW_CardId
        res = requests.post(url=url, json=data)
        dict = res.json()
        self.assertEqual(200, dict["code"])
        self.assertEqual("添加卡成功", dict["msg"])

    def test_add_exist(self):
        data, _ = get_params()
        _, url = get_params()
        res = requests.post(url=url, json=data)
        dict = res.json()
        self.assertEqual(5000, dict["code"])
        self.assertEqual("该卡已添加", dict["msg"])

    def test_add_card02(self):
        data, _ = get_params()
        _, url = get_params()
        data["dataSourceId"] = "Qen"
        res = requests.post(url=url,json=data)
        print(res.text)
        dict = res.json()
        self.assertEqual(100, dict["code"])
        self.assertIn("无权限", dict["msg"])

    def test_add_card03(self):
        data, _ = get_params()
        _, url = get_params()
        data["methodId"] = ""
        res = requests.post(url=url,json=data)
        print(res.json())
        dict = res.json()
        self.assertEqual(301, dict["code"])
        self.assertIn("业务ID不能为空", dict["msg"])


