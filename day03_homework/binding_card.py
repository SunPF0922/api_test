import json

import requests


def get_data():
    data = {"dataSourceId": "endq", "methodId": "01A",
            "cardUser": {
                "userName": "SPF", "idType": "1", "idNumber": "0922"},
            "cardInfo":
                {"cardNumber": "heng2"}}
    return data


def binding_card():  # 首次绑卡 code:5010
    data = get_data()
    url = "http://115.28.108.130:8080/gasStation/process?"
    headers = {"Content-Type": "application/json"}
    res = requests.post(url=url,json=data,headers=headers)
    dict = res.json()
    # print(json.dumps(res_dict,indent=2,ensure_ascii=False))
    # print(res.text)
    return dict


def binding_card02():  # 已注销的卡无法绑定
    data = get_data()
    data["cardInfo"]["CardNumber"] = "11112"
    data["cardUser"]["idNumber"] = "08120922"
    url = "http://115.28.108.130:8080/gasStation/process?"
    res = requests.post(url=url, json=data)
    # print(res.json())
    dict = res.json()
    return dict


def binding_card01():  # 用户第二次绑卡 code:5010
    data = get_data()
    url = "http://115.28.108.130:8080/gasStation/process?"
    data ["cardInfo"]["cardNumber"] = "heng1"
    res = requests.post(url=url, json=data)
    print(res.json())


def binding_card05():  # 同一用户只能绑定两张卡，code:5014
    data = get_data()
    url = "http://115.28.108.130:8080/gasStation/process?"
    data["cardInfo"]["cardNumber"] = "heng4"
    res = requests.post(url=url, json=data)
    print(res.json())


def binding_card03():  # 用户名为空 code:301
    data = get_data()
    url = "http://115.28.108.130:8080/gasStation/process?"
    data["cardUser"]["userName"] = ""
    res = requests.post(url=url, json=data)
    dict = res.json()
    return dict


def binding_card04():  # 证件类型为空 code:5031
    data = get_data()
    url = "http://115.28.108.130:8080/gasStation/process?"
    data["cardUser"]["idType"] = ""
    res = requests.post(url=url, json=data)
    # print(res.json())
    dict = res.json()
    return dict





def binding_card06():
    data = get_data()
    url = "http://115.28.108.130:8080/gasStation/process?"
    res = requests.post(url=url, json=data)
    print(res.json())
    dict = res.json()
    return dict


if __name__ == "__main__":
    # binding_card()
    # binding_card01()
    # binding_card02()
    # binding_card03()
    # binding_card04()
    binding_card05()