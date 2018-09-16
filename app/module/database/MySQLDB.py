#! /usr/bin/env python
# -*- coding: utf-8 -*- 
#
# MySQLDB.py
#
# Created by ruibin.chow on 2017/07/31.
# Copyright (c) 2017年 ruibin.chow All rights reserved.
# 

import mysql.connector.pooling
from Log import Loger
from config import Config


class MySQLDBManager(object):  
    ''' mysql 数据库连接池 '''
    __slots__ = ("__cnxpool", "__cnx", "__instance")
    __instance = None
     
    def __init__(self):  
        ''''' Constructor '''
        dbconfig = {
          "user":Config.DBUSER,
          "password":Config.DBPWD,
          "host":Config.DBHOST,
          "port":Config.DBPORT,
          "database":Config.DBNAME,
          "charset":Config.DBCHAR
        }

        try:  
            self.__cnxpool = mysql.connector.pooling.MySQLConnectionPool(pool_size=Config.DBPOOLSIZE, 
                        pool_reset_session=True, **dbconfig)  
        except Exception as e:  
            Loger.error(e, __file__)
            raise e
    
    @classmethod
    def shareInstanced(cls):
        """单例模式"""
        if(cls.__instance == None):
            cls.__instance = MySQLDBManager()
        return cls.__instance
          
    def executeSingleDml(self, strsql):
        """ insert update delete 单条sql语句"""
        results = True
        try:  
            cnx = self.__cnxpool.get_connection()  
            cursor = cnx.cursor()  
            cursor.execute(strsql)  
            cursor.close()  
            cnx.commit()  
        except Exception as e:  
            Loger.error(e, __file__)
            results = False
            raise e
        finally:  
            if cnx:  
                cnx.close()
        return results

    def executeSingleDmlWithArgs(self, strsql, args):
        """ insert update delete 单条sql语句"""
        results = True
        try:  
            cnx = self.__cnxpool.get_connection()  
            cursor = cnx.cursor()  
            cursor.execute(strsql, args)  
            cursor.close()  
            cnx.commit()  
        except Exception as e:  
            Loger.error(e, __file__)
            results = False
            raise e
        finally:  
            if cnx:  
                cnx.close()
        return results
      
    def executeSingleQuery(self, strsql, dictionary=True): 
        """ 查询 单条sql语句"""
        results = None  
        try:  
            cnx = self.__cnxpool.get_connection()  
            cursor = cnx.cursor(dictionary=dictionary)  
            cursor.execute(strsql)  
            results = cursor.fetchall()  
            cursor.close()  
        except Exception as e:  
            Loger.error(e, __file__)
            raise e
        finally:  
            if cnx:  
                cnx.close()  
        return results  

    def executeSingleQueryWithArgs(self, strsql, args, dictionary=True): 
        """ 查询 单条sql语句"""
        results = None  
        try:  
            cnx = self.__cnxpool.get_connection()  
            cursor = cnx.cursor(dictionary=dictionary)  
            cursor.execute(strsql, args)  
            results = cursor.fetchall()  
            cursor.close()  
        except Exception as e:  
            Loger.error(e, __file__)
            raise e
        finally:  
            if cnx:  
                cnx.close()  
        return results  
      
    def __startTransaction(self):  
        try:  
            self.__cnx = self.__cnxpool.get_connection()  
        except Exception as e:  
            Loger.error(e, __file__)
            raise e
      
    def __endTransaction(self):
        try:
            if self.__cnx:  
                self.__cnx.close()  
        except Exception, e:
            Loger.error(e, __file__)
            raise e
        
      
    def __commitTransaction(self):  
        try:  
            self.__cnx.commit()  
        except Exception as e:  
            Loger.error(e, __file__)
            raise e
      
    def __rollbackTransaction(self):  
        try:  
            self.__cnx.rollback()  
        except Exception as e:  
            Loger.error(e, __file__)
            raise e
      
    def executeTransactionQuery(self, strsql, dictionary=True):
        """ 事务下查询sql语句"""
        results = None
        self.__startTransaction()
        try:  
            cursor = self.__cnx.cursor(dictionary=dictionary)  
            cursor.execute(strsql)  
            results = cursor.fetchall()  
            cursor.close()
            self.__commitTransaction() 
        except Exception as e:  
            Loger.error(e, __file__)
            self.__rollbackTransaction()
            raise e
        finally:
            self.__endTransaction() 

        return results

    def executeTransactionQueryWithArgs(self, strsql, args, dictionary=True):
        """ 事务下查询sql语句"""
        results = None
        self.__startTransaction()
        try:  
            cursor = self.__cnx.cursor(dictionary=dictionary)  
            cursor.execute(strsql, args)  
            results = cursor.fetchall()  
            cursor.close()
            self.__commitTransaction() 
        except Exception as e:  
            Loger.error(e, __file__)
            self.__rollbackTransaction()
            raise e
        finally:
            self.__endTransaction() 

        return results  
      
    def executeTransactionDml(self, strsql):
        """事务下 insert update delete 单条sql语句"""
        results = True
        self.__startTransaction()
        try:  
            cursor = self.__cnx.cursor()  
            cursor.execute(strsql)  
            cursor.close()
            self.__commitTransaction()
        except Exception as e:  
            Loger.error(e, __file__)
            results = False
            self.__rollbackTransaction()
            raise e
        finally:
            self.__endTransaction()
        return results

    def executeTransactionDmlWithArgs(self, strsql, args):
        """事务下 insert update delete 单条sql语句"""
        results = True
        self.__startTransaction()
        try:  
            cursor = self.__cnx.cursor()  
            cursor.execute(strsql, args)  
            cursor.close()
            self.__commitTransaction()
        except Exception as e:  
            Loger.error(e, __file__)
            results = False
            self.__rollbackTransaction()
            raise e
        finally:
            self.__endTransaction()
        return results

    def executeTransactionMutltiDml(self, sqlList):
        """事务下 insert update delete 多条sql语句"""
        results = True
        self.__startTransaction()
        try:  
            cursor = self.__cnx.cursor()  
            for strsql in sqlList:
                cursor.execute(strsql)
            cursor.close()
            self.__commitTransaction()
        except Exception as e:  
            Loger.error(e, __file__)
            results = False
            self.__rollbackTransaction()
            raise e
        finally:
            self.__endTransaction()
        return results
  
    def executeTransactionMutltiDmlWithArgsList(self, sqlList, argsList):
        """事务下 insert update delete 多条sql语句
            argsList 数量与 sqlList数量一致，若无，则该条sql对应为[]
        """
        results = True
        self.__startTransaction()
        try:  
            cursor = self.__cnx.cursor()
            index = 0
            for strsql in sqlList:
                args = argsList[index]
                cursor.execute(strsql, args)
                index +=1
            cursor.close()
            self.__commitTransaction()
        except Exception as e:  
            Loger.error(e, __file__)
            results = False
            self.__rollbackTransaction()
            raise e
        finally:
            self.__endTransaction()
        return results

  
def test():  
    ''''' 事务使用样例 '''  
      
    cnxpool = DBManager.shareInstanced()
      
    results = cnxpool.executeTransactionQuery("SELECT * FROM `t_backoffice_user`")
    for row in results:  
        print "id:%d, name:%s"%(row[0],row[1])
    
    Loger.debug("dsdf")

    sql1 = """INSERT INTO `t_backoffice_user`(`id`, `nickname`, `detail`, `phone`, `email`, `qq`, `wechat`, `gender`, `area`, `avator`, `career`, `time`, `password`,`level`)
    VALUES(4, 'zruibin1234', 'administration', '+8613113324024', 'ruibin.chow@qq.com', '328437740', 'z_ruibin', 1, '深圳', ' ', '程序员', '2017-07-31 06:17:40',
            'f8f235136f525e39e94f401424954c3a', 0);"""
    sql2 = """INSERT INTO `t_backoffice_user`(`id`, `nickname`, `detail`, `phone`, `email`, `qq`, `wechat`, `gender`, `area`, `avator`, `career`, `time`, `password`,`level`)
    VALUES(3, 'zruibin1234', 'administration', '+8613113324024', 'ruibin.chow@qq.com', '328437740', 'z_ruibin', 1, '深圳', ' ', '程序员', '2017-07-31 06:17:40',
            'f8f235136f525e39e94f401424954c3a', 0);"""
    results = cnxpool.executeTransactionMutltiDml([sql1,sql2])  
    print results 
  

if __name__ == '__main__':
    pass













