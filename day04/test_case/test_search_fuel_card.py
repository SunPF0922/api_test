import unittest
import json
import requests

from lib.excel import Excel
class TestSearchFuelCard(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.excel = Excel("加油卡完整用例.xls")
        cls.sheet_data = cls.excel.get_data("查询")


    def test_search_fuel_card(self):
        case_data = self.sheet_data["正常查询"]
        url = case_data["接口地址(名称)URL"]
        expect = json.loads(case_data["预期结果"])
        res = requests.get(url=url)
        print(res.text)
        self.assertEqual("成功返回", res.json()["msg"])
        # self.assertEqual(expect, res.json())


    def test_search_noexist_fuel_card(self):
        url = "http://115.28.108.130:8080/gasStation/process?methodId=02A&userId=6786&cardNumber=1234567890&dataSourceId=bHRz"
        # query yu= {"methodId=02A&userId=6786&cardNumber=1234567890&dataSourceId=bHRz"}
        expect = {"code":200,"msg":"充值成功","result":
            {"cardBalance":"20000","cardNumber":"0987654321","cardStatus":5010,"id":78475776,"userId":6786},
                  "success":True}
        res = requests.get(url=url)
        self.assertEqual(expect, res.text)