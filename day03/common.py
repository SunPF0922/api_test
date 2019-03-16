"""用例辅助方法"""
from lib.db import query_db, update_db

name = "SHM"
def get_user_data(conn,name):
    conn = get_conn()
    result = query_db(conn,"select * from user where name = '{}'".format(name))
    return result

def del_user(conn,sql):
    result = update_db(conn,"delete from user where name = '{}'".format(name))
    return result


if __name__ == "__main__":
    from lib.db import get_conn
    conn = get_conn()
    # del_user()
    print(get_user_data())