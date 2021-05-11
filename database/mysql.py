# ************************************
# -*- coding: utf-8 -*-
# *作者: 周俊                     
# *文件名: mysql.py                
# *创建时间: 2021-05-11 20:36 
# *功能说明:  数据库操作 打开 查询 插入 删除
# *版本: V1.0
# *更新时间: 
# ************************************
import pymysql
DB_HOST = 'localhost'
DB_POST = '3306'
DB_USER = 'root'
DB_PASSWORD = '123231'
DB_NAME = 'press'


class mysql():
    # 打开数据库
    def open_mysql(self):
        try:
            # 连接数据库
            self.db = pymysql.connect(DB_HOST, DB_USER, DB_PASSWORD, DB_NAME)
            # 打开数据库
            self.cur = self.db.cursor()
        except pymysql.Error as e:
            print("数据库错误def_open_mysql:" + str(e))

    # 数据库查询数据
    def find_mysql(self, sql):
        try:
            self.open_mysql()
            self.cur.execute(sql)
            result = self.cur.fetchall()
            self.cur.close()
            return result
        except pymysql.Error as e:
            # 错误信息
            print("错误def_select_find:" + str(e))

    # 数据库插入数据
    def add_mysql(self, sql, value):
        try:
            self.open_mysql()
            # 执行SQL语句
            self.cur.execute(sql, value)
            # 提交数据
            self.db.commit()
            # 关闭表格
            self.cur.close()
            # 关闭数据库
            self.db.close()
        except pymysql.Error as e:
            # 错误信息
            print("错误def_select_find:" + str(e))

    # 数据库删除数据
    def delete_mysql(self, sql):
        try:
            self.open_mysql()
            self.cur.execute(sql)
            self.db.commit()  # 提交请求
            self.cur.close()
            # return result
        except pymysql.Error as e:
            # 错误信息
            print("错误def_select_find:" + str(e))