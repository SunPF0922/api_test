import json  #核心库

import requests



def get(url= "http://www.baidu.com"):
    res = requests.get(url=url)
    print(res.text)



def post_form():
    url = "http://115.28.108.130:5000/api/user/login/"
    data = {"name":"SPF","password":"0922"}
    res = requests.post(url=url,data=data)
    print(res.text)


def post_json_01():
    url = "http://115.28.108.130:5000/api/user/reg/"
    data = {"name": "SPF","password":"0922"}
    res = requests.post(url=url,json=data)
    print(res.json().get("msg"))    # 响应的字典格式，响应不是json会报错


def post_json_02():
    url = "http://115.28.108.130:5000/api/user/reg/"
    data = '''{
    "name": "SPF",
    "password":"0922"
    }'''
    headers = {"Content-Type": "application/json"}
    res = requests.post(url=url, data=data, headers=headers)
    print(res.json().get("msg"))
    # print(res.text)


def post_json_03():
    url = "http://115.28.108.130:5000/api/user/reg/"
    data = {"name": "张三","password":"123456"}
    headers = {"Content-Type": "application/json"}
    res = requests.post(url=url,data=json.dumps(data),headers=headers)
    #print(res.text)
    #print(res.json().get("msg"))
    res_dict = res.json() # 字典格式
    print(json.dumps(res_dict, indent=2, ensure_ascii=False,sort_keys=True)) # ensure_ascii=False，确保输出的是转码后的，不是\u的格式


def post_xml():
    url = "http://httpbin.org/post"
    data = '''<xml><name>SPF</name></xml>
    '''
    headers = {"Content-Type":"application/xml"}
    res = requests.post(url=url, data=data, headers=headers)
    print(res.text)


def post_file():
    url = "http://115.28.108.130:5000/api/user/uploadImage/"
    files = {"file":open("1.txt","rb")} #"rb"代表二进制格式打开文件，也可打开图片
    res = requests.post(url=url,files=files)
    print(res.text)


def get_basic_auth():
    url = "http://115.28.108.130:5000/api/user/login2/"
    res = requests.get(url=url,auth=("admin", "secret"))
    print(res.text)


# def get_user_List():
#     #cookie = "PYSESSID=896f1ec4-3801-11e9-85c3-00163e06e52c; session=eyI4OTZmMWVjNC0zODAxLTExZTktODVjMy0wMDE2M2UwNmU1MmMiOnRydWV9.D1PR_g.PWJstDbOuuUj7_3NXxWGWJczvoo"
#     url2 ="http://115.28.108.130:5000/api/user/getUserList/"
#     res2 = requests.get(url=url2,cookies=cookie)
#     print(res2.text)


def get_user_List1():
    #cookie = "PYSESSID=896f1ec4-3801-11e9-85c3-00163e06e52c; session=eyI4OTZmMWVjNC0zODAxLTExZTktODVjMy0wMDE2M2UwNmU1MmMiOnRydWV9.D1PR_g.PWJstDbOuuUj7_3NXxWGWJczvoo"
    url1= "http://115.28.108.130:5000/api/user/login/"
    data = {"name":"SPF","password":"0922"}
    res1 = requests.post(url=url1,data=data)
    print(res1.cookies)
    url2 ="http://115.28.108.130:5000/api/user/getUserList/"
    res2 = requests.get(url=url2,cookies=res1.cookies)
    print(res2.text)


def get_user_List2():
    #cookies 拆分成字典格式，不能用字符串去传
    cookies = {
        "PYSESSID":"896f1ec4-3801-11e9-85c3-00163e06e52c",
        "session":"eyI4OTZmMWVjNC0zODAxLTExZTktODVjMy0wMDE2M2UwNmU1MmMiOnRydWV9.D1PR_g.PWJstDbOuuUj7_3NXxWGWJczvoo"}
    url2 = "http://115.28.108.130:5000/api/user/getUserList/"
    res = requests.get(url=url2, cookies=cookies)
    print(res.text)


def get_user_List3():
    url2 = "http://115.28.108.130:5000/api/user/getUserList/"
    #cookie作为headers的一项，不用拆分
    headers ={"cookie":"PYSESSID=896f1ec4-3801-11e9-85c3-00163e06e52c; session=eyI4OTZmMWVjNC0zODAxLTExZTktODVjMy0wMDE2M2UwNmU1MmMiOnRydWV9.D1PR_g.PWJstDbOuuUj7_3NXxWGWJczvoo"}
    res = requests.get(url=url2, headers=headers)
    print(res.text)


def get_user_List4():
    session = requests.session() #新建一个会话
    url1= "http://115.28.108.130:5000/api/user/login/"
    data = {"name":"SPF","password":"0922"}
    session.post(url=url1,data=data)
    #print(res1.cookies)
    url2 ="http://115.28.108.130:5000/api/user/getUserList/"
    res2 = session.get(url=url2)
    print(res2.text)


def login(username,password):
    session = requests.session()
    url = "http://115.28.108.130:5000/api/user/login/"
    data = {"name":username,"password":password}
    session.post(url=url,data=data)
    return session


def get_user_List5():
    s = login("SPF","0922")
    url2 = "http://115.28.108.130:5000/api/user/getUserList/"
    res2 = s.get(url=url2)
    print(res2.text)


def get_token1():
    session = requests.session()
    url = "http://115.28.108.130:5000/api/user/getToken/?appid=136425"
    res =requests.get(url=url)
    print(res.text)
    token = (res.text).split("=")[1]
    print(token)
    url1 = "http://115.28.108.130:5000/api/user/updateUser/?token={}".format(token)
    print(url1)
    data = {"name":"SPF","password":"0922"}
    res= requests.post(url=url1,json=data)
    #print(res.text)
    print(res.json())


def get_token():
    url = "http://115.28.108.130:5000/api/user/getToken/?appid=136425"
    res = requests.get(url=url)
    print(res.text)
    token = res.text.split("=")[1]
    return token


def update_user():
    token = get_token()
    url = "http://115.28.108.130:5000/api/user/updateUser/?token={}".format(token)
    data = {
        "name": "SPF", "password": "0922"
    }
    res = requests.post(url=url,json=data)
    print(res.json())


def get_tulin():
    text = ["你好啊","12345","你几岁"]
    i =0
    for i in text:
        url = "http://www.tuling123.com/openapi/api?key=ec961279f453459b9248f0aeb6600bbe&info={}".format(i)
        res = requests.get(url=url)
    print(url)
    print(res.text)

def batch_reg():
    users = ["SPF01","SPF02","孙佩芬03"]
    url = "http://115.28.108.130:5000/api/user/reg/"
    data = {"name": "SPF","password":"0922"}
    for user in users:
        data["name"] = user
        res = requests.post(url=url,json=data)
        print(res.json())    # 响应的字典格式，响应不是json会报错


if __name__ == "__main__":


    # get()
    # post_form()
    # post_json_01()
    #post_json_02()
    # post_json_03()
    #post_xml()
    #post_file
    #get_basic_auth()
    #get_user_List1()
    #get_user_List2()
    #get_user_List3()
    get_user_List4()
    # get_user_List5()
    #get_token1()
    #update_user()
    # get_tulin()
    #batch_reg()




