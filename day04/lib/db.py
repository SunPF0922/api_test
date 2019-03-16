import pymysql
import logging

from config import DB_CONFIG


class DB(object):
    def __init__(self):  # 初始化方法
        self.conn = pymysql.connect(**DB_CONFIG)
        self.cur = self.conn.cursor()

    def query(self, sql):
        logging.debug("查询SQL:{}".format(sql))
        self.cur.execute(sql)
        result = self.cur.fetchall()  # fetchall返回结果为嵌套元组（（1,....,,2222),(2,....,999))
        logging.debug("查询结果:{}".format(result))
        return result

    def execute(self, sql):
        logging.debug("执行SQL:{}".format(sql))
        try:
            self.cur.execute(sql)
        except Exception as ex:
            logging.debug(str(ex))
            self.conn.rollback()  # 回滚机制，有异常时回滚

    def is_card_exist(self, card_number):  # self代表当前对象，card_number是方法的参数
        logging.debug("查询卡：{}是否存在".format(card_number))
        sql = "select cardNumber from cardinfo where cardNumber = '{}'".format(card_number)
        result = self.query(sql)  # self代表当前对象，调用query方法

        if result:  # 空返回（） 非空：（（...））
            logging.debug("该卡存在")
            return result
        else:
            logging.debug("该卡不存在")
            return False

    def del_card_if_exist(self, card_number):
        logging.debug("删除卡：{}".format(card_number))
        sql1 = "delete from cardinfo where cardNumber = '{}'".format(card_number)
        if self.is_card_exist(card_number):
            self.execute(sql1)
            logging.debug("删除成功")
        # return True if result else False


if __name__ == "__main__":
    db = DB()
    db.is_card_exist("heng")
    # db.del_card_if_exist("heng")
    # db.query()
