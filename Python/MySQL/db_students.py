# -*- coding: utf-8 -*-
"""
Created on Sun Sep 30 12:19:31 2018

@author: 小周

"""

import sqlite3
#import mysql.connector
#from mysql.connector import errorcode

def show_info_friends():
    cnx = mysql.connector.connect(user='root', password='123', database='students', buffered=True)
    cursor = cnx.cursor(buffered=True)
    query = ("select * from friends where age < 23 order by id")
    cursor.execute(query)
    wordList = []
    print('ID','\t 姓名', '\t性别', '\t年龄', '\t电话号码')
    for info in cursor:
        wordList.append([info[0], info[1], info[2], info[3], info[4]])
        
    for item in wordList:
        print(item[0], '\t', item[1], '\t', item[2], '\t', item[3], '\t', item[4])
    cursor.close()
    cnx.close()

class DataBaseConnection:
    def __init__(self, dbName):
        '''
        Parameters:
        -----------
        dbName: 要操作数据库的名字
        
        '''
        # 构造方法,连接数据库
        self._conn = sqlite3.connect(dbName)
        
    def __del__(self):
        # 析构方法，关闭数据库连接
        self._conn.close()
        
    def __process(self, s):
        '''
        Parameters
        ------------
        s: 字符串型的字典值
        用来处理SQL语句中的字符串型的字典值
        在两侧加双引号
        
        Returns
        ------------
        s
        '''
        if isinstance(s, str):
            return '"' + s + '"'
        return str(s)
    
    def insert(self, table, *values):
        '''
        插入数据
        
        Parameters
        -----------
        table: 要插入的表名
        values：要插入的数据
        '''
        # 构造SQL语句
        sql = 'INSERT INTO ' + table + ' VALUES('
        if values:
            for item in values[:-1]:
                sql = sql + self.__process(item) + ','
            sql = sql + self.__process(values[-1]) + ')'
            # 执行SQL语句
            self._conn.execute(sql)
            # 提交事务，确认插入
            self._conn.commit()
        else:
            print('Nothing to insert')

    def delete(self, table, **kwargs):
        '''
        删除数据
        
        Parameters
        -----------
        table: 要删除的数据所在表名
        kwargs：用来指定约束条件
        '''
        # 构造SQL语句
        sql = 'DELETE FROM ' + table
        if kwargs:
            sql = sql + ' WHERE '
            for key, value in kwargs.items():
                sql = sql + key + '=' + self.__process(value) + ' and '
            sql = sql[:-5]
        else:
            # 不加WHERE就删除，就要确认一下
            flag=''
            while flag not in ('y', 'n'):
                flag = input('你确定不加where嘛?(y/n):').lower()
            if flag == 'n':
                print('删除操作取消.')
                return
        self._conn.execute(sql)
        self._conn.commit()
    
    def update(self, table, conditionKey=None, conditionValue=None, **kwargs):
        '''
        更新数据
        
        Parameters
        -----------
        table: 要更新的表名
        conditionKey：约束字段
        conditionValue：约束字典的值
        kwargs：要更新的字段和值
        '''
        if not kwargs:
            print('Nothing to update')
            return
        # 构造SQL语句
        sql = 'UPDATE ' + table + ' SET '
        for key, value in kwargs.items():
            sql = sql + key + '=' + self.__process(value) + ' and '
        sql = sql[:-5]
        if conditionKey is None:
            # # 不加WHERE就删除，就要确认一下
            flag=''
            while flag not in ('y', 'n'):
                flag = input('你确定不加where嘛?(y/n):').lower()
            if flag == 'n':
                print('删除操作取消.')
                return
        else:
            sql = sql + ' WHERE ' + conditionKey + '='
            if isinstance(conditionValue, str):
                sql = sql + self.__process(conditionValue)
        self._conn.execute(sql)
        self._conn.commit()
    
    def selete(self, table, **kwargs):
        '''
        查询数据
        
        Parameters
        -----------
        table: 要查询数据的表名
        kwargs：约束条件
        
        Return
        -----------
        返回更新成功的列表
        '''
        sql = 'SELECT * FROM ' + table
        if kwargs:
            sql = sql + ' WHERE '
            for key, value in kwargs.items():
                sql = sql + key + '=' + self.__process(value) + ' and '
            sql = sql[:-5]
        return list(self._conn.execute(sql))

cn = DataBaseConnection('students.db')

#cn.selete('mytest')






