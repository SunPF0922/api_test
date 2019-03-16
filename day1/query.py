import requests


def get_card():
    url = "http://115.28.108.130:8080/gasStation/process"
    data = {"methodId":"02A","userId":"8751","cardNumber":"1282520443","dataSourceId":"endq"}
    res = requests.get(url=url,params=data)
    print(res.text)


if __name__ == "__main__":
    get_card()


