import pymysql
from config import DB_API_TEST
# 查询


def get_conn(db_conf=DB_API_TEST):
    conn = pymysql.connect(**db_conf)
    return conn


def query_db(conn,sql):
    # 1、建立连接
    # conn = pymysql.connect(**DB_API_TEST)


# 2、建立游标，指向缓存区的一个变量
    cur = conn.cursor()

# 3、执行SQL
    cur.execute(sql)

# 4、获取缓存区中的数据
    result1 = cur.fetchone()
# result2 = cur.fetchall()
    print(result1[1])  # 取元组中的某一个数据

# 5、关闭连接
    conn.close()


def change_db(conn,sql):
    # 1、建立连接
    conn = pymysql.connect(host="115.28.108.130",
                           port=3306,
                           user="test_case",
                           password="123456",
                           db="api_test",
                           charset="utf8")

    # 2、建立游标，指向缓存区的一个变量
    cur = conn.cursor()

    # 3、执行SQL
    cur.execute(sql)

    # 提交更改
    conn.commit()

    # 5、关闭连接
    conn.close()


def update_db(conn,sql):
    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()


if __name__ == "__main__":
    conn = get_conn()
    sql = 'INSERT INTO `user` VALUES (41005,"孙恒茂","0101")'
    sql1 = 'select * from user where id = 41002'
    # update_db(conn,sql)
    # query_db(conn,sql1)
    change_db(conn,'delete from  `user` where id = 41002)')