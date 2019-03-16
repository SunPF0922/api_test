import requests


def get_param():
    url = "http://115.28.108.130:8080/gasStation/process?"
    data = {"methodId": "02A", "userId": "8751", "cardNumber": "1282520441", "dataSourceId": "endq"}
    return data, url


def get_card():  # 卡号不存在
    url = "http://115.28.108.130:8080/gasStation/process?"
    data = {"methodId": "02A", "userId": "8751", "cardNumber": "1282520", "dataSourceId": "endq"}
    res = requests.get(url=url,params=data)
    print(res.text)


def get_card01():  # 无第三方接口权限
    url = "http://115.28.108.130:8080/gasStation/process?"
    data = {"methodId": "02A", "userId": "8751", "cardNumber": "1282520441", "dataSourceId": "endq11"}
    res = requests.get(url=url,params=data)
    print(res.text)


def get_card03():  # 业务ID错误
    url = "http://115.28.108.130:8080/gasStation/process?"
    data = get_param()
    # data = {"methodId": "000", "userId":"8751", "cardNumber":"1282520441", "dataSourceId":"endq"}
    data["methodId"] = "000"  # 报错信息 data["methodId"] = "000" TypeError: 'str' object does not support item assignment
    res = requests.get(url=url,params=data)
    print(res.text)


def get_card04():  # 正常查询
    url = "http://115.28.108.130:8080/gasStation/process?"
    data = get_param()
    res = requests.get(url=url,params=data)
    print(res.text)


def get_card05():  # 业务ID无效 code:199
    data, _ = get_param()
    _, url = get_param()
    # url = "http://115.28.108.130:8080/gasStation/process?"
    data ["methodId"] = "000"
    res = requests.get(url=url, params=data)
    print(res.text)


def get_card06():
    data, _ = get_param()
    _, url = get_param()
    data["dataSourceId"] = "endq111"
    res = requests.get(url=url,params=data)
    print(res.text)


if __name__ == "__main__":
    # get_card()
    # get_card01()
    # get_cadr02()
    # get_card03()
    # get_card04()
    # get_card05()
    get_card06()

