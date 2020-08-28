import pymysql
from common.config import *


class DoMysql:
    def __init__(self):
        user = config.get("mysql", "user")
        password = config.get("mysql", "password")
        host = config.get("mysql", "host")
        port = int(config.get("mysql", "port"))

        self.mysql = pymysql.connect(user=user, password=password, host=host, port=port)
        self.cursor = self.mysql.cursor(pymysql.cursors.DictCursor)

    def fetchone(self, sql):
        self.cursor.execute(sql)
        # 强制提交一下，避免数据库更新不及时
        self.mysql.commit()
        return self.cursor.fetchone()

    def fetchall(self, sql):
        self.cursor.execute(sql)
        self.mysql.commit()
        return self.cursor.fetchall()

    def close(self):
        self.cursor.close()
        self.mysql.close()