#! /usr/bin/env python
# -*- coding: utf-8 -*- 
#
# SQLiteDB.py
#
# Created by ruibin.chow on 2017/07/31.
# Copyright (c) 2017年 ruibin.chow All rights reserved.
# 

from Log import Loger
from config import Config


class SQLiteDBManager(object):  
    ''' mysql 数据库连接池 '''
    __slots__ = ("__cnxpool", "__cnx", "__instance")
    __instance = None
     
    def __init__(self):  
        ''''' Constructor '''
        dbconfig = {

        }

        try:  
           pass 
        except Exception as e:  
            Loger.error(e, __file__)
            raise e
    
    @classmethod
    def shareInstanced(cls):
        """单例模式"""
        if(cls.__instance == None):
            cls.__instance = SQLiteDBManager()
        return cls.__instance
          

  

if __name__ == '__main__':
    pass













