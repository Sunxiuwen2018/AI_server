#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:SunXiuWen
# make_time:2018/11/30
"""为前端提供音频数据信息"""
from flask import Blueprint
from flask import jsonify
from settings import DB

content = Blueprint("content", __name__)


@content.route("/content_list")
def get_contents():
    content_list = list(DB.contens.find({}))  # 获取全部，必须要list或for
    for index, content_info in enumerate(content_list):
        # "_id" : ObjectId("5b151f8536409809ab2e6b26") 不能被Json序列化，需要转化
        content_list[index]["_id"] = str(content_list[index]["_id"])
    return jsonify(content_list)
