#! /usr/bin/env python
# -*- coding: utf-8 -*- 
#
# SQLiteDB.py
#
# Created by ruibin.chow on 2017/07/31.
# Copyright (c) 2017年 ruibin.chow All rights reserved.
# 

from Log import *
import sqlite3


class SQLiteDBManager(object):  
    ''' mysql 数据库连接池 '''
    __slots__ = ("__conn", "__instance")
    __instance = None
     
    def __init__(self):  
        ''''' Constructor '''
        # try:  
        #     sqlite3
        # except Exception as e:  
        #     Loger.error(e, __file__)
        #     raise e
        pass
    
    @classmethod
    def shareInstanced(cls):
        """单例模式"""
        if(cls.__instance == None):
            cls.__instance = SQLiteDBManager()
        return cls.__instance

    def setDBPath(self, path):
        self.__conn = sqlite3.connect(path)

    def executeDml(self, strsql):
        self.__conn.execute(strsql)
        self.__conn.commit()

    def executeDmlWithArgs(self, strsql, args):
        self.__conn.executemany(strsql, args)
        self.__conn.commit()
          
    def executeQuery(self, strsql):
        curson = self.__conn.execute(strsql)
        self.__conn.commit()
        rows = curson.fetchall()
        return rows

    def executeQueryWithArgs(self, strsql, args):
        curson = self.__conn.executemany(strsql, args)
        self.__conn.commit()
        rows = curson.fetchall()
        return rows

  

if __name__ == '__main__':
    pass













