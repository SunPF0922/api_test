import requests

import json


def get_data():
    data = {"methodId": "00A", "dataSourceId": "endq", "CardInfo": {"cardNumber": "09223"}}
    return data


def reg_card():  # 添加成功 code:200
    data = get_data()
    url = "http://115.28.108.130:8080/gasStation/process?"
    res = requests.post(url=url, json=data)
    print(res.json())


def reg_card01():  # 重复添加code:5000
    data = get_data()
    url = "http://115.28.108.130:8080/gasStation/process?"
    res = requests.post(url=url, json=data)
    print(res.json())


def reg_card02():  # 卡号为空,code:5000
    data = get_data()
    url = "http://115.28.108.130:8080/gasStation/process"
    data["CardInfo"]["cardNumber"] = ""
    res = requests.post(url=url,json=data)
    print(res.json())


def reg_card03():  # 业务ID无效 code:199
    data = get_data()
    url = "http://115.28.108.130:8080/gasStation/process"
    data["methodId"] = "000"
    res = requests.post(url=url,json=data)
    print(res.json())


def reg_card04():  # 业务为空 code:301
    data = get_data()
    url = "http://115.28.108.130:8080/gasStation/process"
    data["methodId"] = ""
    res = requests.post(url=url,json=data)
    print(res.json())


if __name__ == "__main__":
    # reg_card()
    # reg_card01()
    # reg_card02()
    reg_card03()
    reg_card04()

