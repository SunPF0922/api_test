import json

import requests


def get_data():
    data = {"methodId": "03A", "dataSourceId": "endq",
            "cardInfo":
                {"cardNumber": "1282520441", "cardBalance": "5000"}
            }
    url = "http://115.28.108.130:8080/gasStation/process?"
    return data
    return url


def add_balance():
    url = "http://115.28.108.130:8080/gasStation/process?"
    data = {"methodId":"03A", "dataSourceId":"endq",
            "cardInfo":
                {"cardNumber":"1282520441", "cardBalance":"5000"}
            }
    res = requests.post(url=url, json=data)
    print(res.json())
    # res_dict = res.json()
    # print(json.dumps(res_dict, indent=2, ensure_ascii=False))


def add_balance01():
    url = "http://115.28.108.130:8080/gasStation/process?"
    data = {"methodId":"000", "dataSourceId":"endq",
            "cardInfo":
                {"cardNumber":"1282520441", "cardBalance":"5000"}
            }
    headers = {"Content-Type": "application/json"}
    res = requests.post(url=url, json=data, headers=headers)
    print(res.text)


def get_data():
    data = {"methodId": "03A", "dataSourceId": "endq",
            "cardInfo":
                {"cardNumber": "1282520441", "cardBalance": "5000"}
            }
    url = "http://115.28.108.130:8080/gasStation/process?"
    return data
    return url


def add_balance02():  # 加油卡不存在，code：5013
    data = get_data()
    url = "http://115.28.108.130:8080/gasStation/process?"
    data["cardInfo"]["cardNumber"] = "0922"
    res = requests.post(url=url, json=data)
    print(res.json())


def add_balance03():
    data = get_data()
    url = "http://115.28.108.130:8080/gasStation/process?"
    data["dataSourceId"] = "qwe"
    res = requests.post(url=url, json=data)
    print(res.json())


if __name__ == "__main__":
    add_balance()
    # add_balance01()
    # add_balance02()
    # add_balance03()


