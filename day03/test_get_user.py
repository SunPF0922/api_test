import unittest
import requests


def test_get_userlist1():
    url = "http://115.28.108.130:5000/api/user/login/"
    data = {"name": "SHM", "password": "0101"}
    session = requests.session()
    session.post(url=url, data=data)
    url1 = "http://115.28.108.130:5000/api/user/getUserList/"
    res = session.get(url=url1)
    print(res.text)



class Test_get_userlist(unittest.TestCase):

    def test_get_userlist(self):
        url = "http://115.28.108.130:5000/api/user/login/"
        data = {"name": "SHM", "password": "0101"}
        session = requests.session()
        session.post(url=url,data=data)
        url1 = "http://115.28.108.130:5000/api/user/getUserList/"
        res = session.get(url=url1)
        self.assertIn("李天一",res.text)

if __name__ == "__main__":
    pass




