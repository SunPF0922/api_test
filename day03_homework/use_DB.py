import pymysql

from db_config import DB_CONFIG

def get_conn():
    conn = pymysql.connect(**DB_CONFIG)
    return conn


def query_db(conn, sql):
    cur = conn.cursor()
    cur.execute(sql)
    result = cur.fetchone()
    cur.close()
    return result

def change_db(conn, sql):
    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()


if __name__ == "__main__":
    conn = get_conn()
    query_db(conn,'SELECT * FROM cardinfo WHERE cardNumber = "0922"')
   # change_db(conn,'DELETE FROM cardinfo WHERE cardNumber = "0922"')



