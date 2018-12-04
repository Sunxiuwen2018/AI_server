#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:SunXiuWen
# make_time:2018/11/30
import os
import pymongo

# 爬取的数据保存目录
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
IMAGES_PATH = os.path.join(BASE_DIR, "Images")
MUSICS_PATH = os.path.join(BASE_DIR, "Musics")

# 数据库的配置
my_client = pymongo.MongoClient(host="127.0.0.1", port=27017)
DB = my_client["db_ai"]

# 初始化返回值规范
"""
code: 0  表示成功， 非0 异常
"""
RESPONSE_ = {
    "code": 0,
    'msg': "",
    "data": {}
}
