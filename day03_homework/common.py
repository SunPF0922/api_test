import requests

from use_DB import query_db,change_db,get_conn

cardId = "0922"
def get_card(conn, cardId):
    conn = get_conn()
    result = query_db(conn, "SELECT * FROM cardinfo WHERE cardNumber = '{}'". format(cardId))
    print(result)
    return result


def del_card(conn, cardId):
    conn = get_conn()
    result = change_db(conn, "DELETE FROM cardinfo WHERE cardNumber = '{}'".format(cardId))


def get_card_user(conn,cardId):
    conn = get_conn()
    result = query_db(conn,"SELECT * FROM cardinfo where cardNumber = '{}'".format(cardId))
    print(result)


if __name__ == "__main__":
    conn = get_conn()
    # get_card(conn,cardId)
    get_card_user(conn,"0922")

