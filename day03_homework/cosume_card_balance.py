import json

import requests


def get_param():  # 返回data数据
    data = {"methodId": "04A", "dataSourceId": "endq", "cardInfo": {
        "cardNumber": "1282520441", "cardBalance": "500"
    }, "cardUser": {
        "userId": "8751"
    }}
    return data


def cosume_card():  # 正常消费
    data = get_param()
    url = "http://115.28.108.130:8080/gasStation/process?"
    res = requests.post(url=url, json=data)
    # print(res.json())
    dict = res.json()
    return dict


def cosume_card01():  #消费金额为空
    data = get_param()
    url = "http://115.28.108.130:8080/gasStation/process?"
    data["cardInfo"]["cardBalance"] = ""
    res = requests.post(url=url, json=data)
    # res_dict = res.json()
    # print(json.dumps(res_dict,indent=2,ensure_ascii=False))
    # print(res.json())
    dict = res.json()
    return dict


def cosume_card02():  # code:5013,根据用户ID没有查询到卡号
    data = get_param()
    url = "http://115.28.108.130:8080/gasStation/process?"
    data["cardUser"]["userId"] = "123"
    res = requests.post(url=url, json=data)
    print(res.json())
    dict = res.json()
    return dict


def cosume_card03():  # code:612,消费金额不是整数
    data = get_param()
    url = "http://115.28.108.130:8080/gasStation/process?"
    data ["cardInfo"]["cardBalance"] = "-9"
    res = requests.post(url=url, json=data)
    # print(res.json())
    dict = res.json()
    return dict


def cosume_card04():  # 不提交任何参数发送请求
    data = {}
    url = "http://115.28.108.130:8080/gasStation/process?"
    res = requests.post(url=url, json=data)
    # print(res.json())
    dict = res.json()
    return dict


if __name__ == "__main__":
    # cosume_card()
    # cosume_card01()
    # cosume_card02()
    # cosume_card03()
    cosume_card04()