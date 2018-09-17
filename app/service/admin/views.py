#! /usr/bin/env python
# -*- coding: utf-8 -*- 
#
# views.py
#
# Created by zruibin on 2017/07/24.
# Copyright (c) 2017年 zruibin All rights reserved.
# 

from . import admin
from config import *
from Log import *
from SQLiteDB import SQLiteDBManager

@admin.route('/')
def index():                         
        #  print'__name__',__name__
        # LogE("Admin_TAG", "error----", __file__)
        Loger.error("Admin_TAG", "error----", __file__)
        print Config.SQLiteDB
        print SQLiteDBManager.shareInstanced().executeQuery("SELECT * FROM comment;")
        return '<h1>Hello zruibin, From Service Admin!</h1>'
