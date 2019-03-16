import pymysql

conn = pymysql.connect(host="115.28.108.130",
                       port=3306,
                       user="test_case",
                       password="123456",
                       db="api_test",
                       charset="utf8")

cur = conn.cursor()

cur.execute("SELECT id FROM `user` WHERE name='马瑞雪'")

result = cur.fetchone()
print(result)