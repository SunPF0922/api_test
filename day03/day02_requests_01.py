import json

import requests

def todo_list():
    url = "http://115.28.108.130:5000/todos"
    res = requests.get(url=url)
    print(res.text)


def todo_task():
    url = "http://115.28.108.130:5000/todos"
    data = {"task":"不要熬夜"}
    res = requests.post(url=url,json=data)
    # res_dict = res.json()
    # print(res.json()["task"])
    print(res.json().get("task"))


if __name__ == "__main__":
    # todo_list()
    todo_task()

