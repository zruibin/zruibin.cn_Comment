#! /usr/bin/env python
# -*- coding: utf-8 -*- 
#
# query.py
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
from common.tools import getValueFromRequestByKey, parsePageIndex


@comment.route('/query')
def commentQuery():
    articleUUID = getValueFromRequestByKey("article_uuid")
    index = getValueFromRequestByKey("index")
    if articleUUID == None:
        return RESPONSE_JSON(CODE_ERROR_MISS_PARAM)
    index = parsePageIndex(index)   
    return __queryComment(articleUUID, str(index-1))


def __queryComment(articleUUID, index):
    dataList = None

    querySQL = """SELECT uuid, article_uuid, content, nickname, time 
                FROM comment WHERE article_uuid='%s' 
                ORDER BY time DESC LIMIT %s OFFSET %s""" % (articleUUID, str(Config.PAGE_OF_SIZE), index)
    # print querySQL
    dbManager = SQLiteDBManager.shareInstanced()
    try: 
        dataList = dbManager.executeQuery(querySQL)
        dataList = __queryReplyComment(dataList)
    except Exception as e:
        LogE("COMMENT_TAG", e, __file__)
        return RESPONSE_JSON(CODE_ERROR_SERVICE)
    else:
        return RESPONSE_JSON(CODE_SUCCESS, dataList)


def __queryReplyComment(dataList):
    replyCommentKeyList = []
    for data in dataList:
        replyCommentKeyList.append(data["uuid"])

    if len(replyCommentKeyList) == 0: return dataList

    inString = "'" + "','".join(replyCommentKeyList) + "'"
    queryReplyKeySQL = """
            SELECT uuid, comment_uuid, content, nickname, time FROM reply_comment 
            WHERE comment_uuid IN (%s) ORDER BY time ASC;
        """ % inString

    dbManager = SQLiteDBManager.shareInstanced()
    try: 
        replyDataList = dbManager.executeQuery(queryReplyKeySQL)
        for data in dataList:
            uuid = data["uuid"]
            replyList = []
            for reply in replyDataList:
                if reply["comment_uuid"] == uuid:
                    replyList.append(reply)

            data["replyList"] = replyList
    except Exception as e:
        LogE("COMMENT_TAG", e, __file__)
        raise e

    return dataList
