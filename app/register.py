#! /usr/bin/env python
# -*- coding: utf-8 -*- 
#
# register.py
#
# Created by zruibin on 2017/07/24.
# Copyright (c) 2017年 zruibin All rights reserved.
# 

"""

"""
from service.admin import admin

def registerBlueprint(app):
    """ 注册蓝图，并指定前缀""" 
    app.register_blueprint(admin, url_prefix='/admin')

    

if __name__ == '__main__':
    pass


