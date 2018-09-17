#! /usr/bin/env python
# -*- coding: utf-8 -*- 
#
# insert.py
#
# Created by ruibin.chow on 2018/09/17.
# Copyright (c) 2018年 ruibin.chow All rights reserved.
# 

"""

"""

from service.comment import comment
from config import *
from Log import *
from SQLiteDB import SQLiteDBManager
from common.code import *
from common.tools import getValueFromRequestByKey, parsePageIndex, generateUUID, generateCurrentTime


@comment.route('/insertComment', methods=["POST", "GET"])
def commentInsert():
    articleUUID = getValueFromRequestByKey("article_uuid")
    content = getValueFromRequestByKey("content")
    nickname = getValueFromRequestByKey("nickname")
    email = getValueFromRequestByKey("email")
    # print articleUUID, str(content), str(nickname), email
    if articleUUID == None or content == None or nickname == None or email == None:
        return RESPONSE_JSON(CODE_ERROR_MISS_PARAM)
    if len(articleUUID) == 0 or len(content) == 0 or len(nickname) == 0 or len(email) == 0:
        return RESPONSE_JSON(CODE_ERROR_CONTENT_IS_NULL)
    return __insertComment(articleUUID, content, nickname, email)


def __insertComment(articleUUID, content, nickname, email):
    uuid = generateUUID()
    time = generateCurrentTime()

    insertSQL = """
            INSERT INTO comment (uuid, article_uuid, content, nickname, email, time)
            VALUES ('%s', '%s', '%s', '%s', '%s', '%s');
        """ % (uuid, articleUUID, content, nickname, email, time)

    dbManager = SQLiteDBManager.shareInstanced()
    try: 
        dbManager.executeDml(insertSQL)
    except Exception as e:
        LogE("COMMENT_TAG", e, __file__)
        return RESPONSE_JSON(CODE_ERROR_SERVICE)
    else:
        return RESPONSE_JSON(CODE_SUCCESS)



@comment.route('/insertReplyComment', methods=["POST", "GET"])
def replyCommentInsert():
    articleUUID = getValueFromRequestByKey("article_uuid")
    commentUUID = getValueFromRequestByKey("comment_uuid")
    content = getValueFromRequestByKey("content")
    nickname = getValueFromRequestByKey("nickname")
    email = getValueFromRequestByKey("email")
    # print articleUUID, commentUUID, str(content), str(nickname), email
    if articleUUID == None or content == None or nickname == None or email == None or commentUUID == None:
        return RESPONSE_JSON(CODE_ERROR_MISS_PARAM)
    if len(articleUUID) == 0 or len(content) == 0 or len(nickname) == 0 or len(email) == 0 or len(commentUUID) == 0:
        return RESPONSE_JSON(CODE_ERROR_CONTENT_IS_NULL)
    return __insertReplyComment(articleUUID, commentUUID, content, nickname, email)


def __insertReplyComment(articleUUID, commentUUID, content, nickname, email):
    uuid = generateUUID()
    time = generateCurrentTime()

    insertSQL = """
            INSERT INTO reply_comment (uuid, comment_uuid, article_uuid, content, nickname, email, time)
            VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s');
        """ % (uuid, commentUUID, articleUUID, content, nickname, email, time)

    dbManager = SQLiteDBManager.shareInstanced()
    try: 
        dbManager.executeDml(insertSQL)
    except Exception as e:
        LogE("COMMENT_TAG", e, __file__)
        return RESPONSE_JSON(CODE_ERROR_SERVICE)
    else:
        return RESPONSE_JSON(CODE_SUCCESS)







