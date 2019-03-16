import json

import unittest

from cosume_card_balance import cosume_card,cosume_card01,cosume_card02,cosume_card03,cosume_card04


class TestCosumeCard(unittest.TestCase):
    def test_cosume_normal(self):
        dict = cosume_card()
        self.assertEqual(200, dict["code"])
        self.assertEqual("消费成功!", dict["msg"])

    def test_cosume_none(self):
        dict = cosume_card01()
        self.assertEqual(300, dict["code"])
        self.assertIn("不能为空", dict["msg"])

    def test_cosume03(self):
        dict = cosume_card02()
        self.assertEqual(5013, dict["code"])
        self.assertIn("没有查询到卡号", dict["msg"])

    def test_cosume04(self):
        dict = cosume_card04()
        self.assertEqual(301, dict["code"])
        self.assertIn("不能为空", dict["msg"])
        self.assertIsNone(None, dict["object"])
