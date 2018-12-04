#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:SunXiuWen
# make_time:2018/11/30
"""
爬虫：主要用于采集音频,从喜马拉雅上爬取儿童音频
"""
import requests  # 模拟浏览器发请求
import os  # 解释器与操作系统之间交互
from uuid import uuid4  # 命名
from settings import (IMAGES_PATH, MUSICS_PATH)
from settings import DB

# 获取喜马拉雅音频api接口
xmly_url = "http://m.ximalaya.com/tracks/%s.json"

# 获取喜马拉雅官网地址
music_url_list = ["/ertong/257813/138077771",
                  "/ertong/257813/138347675",
                  "/ertong/257813/140443659",
                  "/ertong/257813/134194026",
                  "/ertong/424529/7713564",
                  '/ertong/424529/7713681',
                  "/ertong/424529/7713660"]

# 获取music的id
for i in music_url_list:
    music_id = i.rsplit("/", 1)[-1]

    res = requests.get(xmly_url % music_id)  # 获取音频的所有信息，以json的字典返回，res.json()
    music_info = res.json()
    music_dict = {
        "title": music_info.get("title"),  # 音频歌名  【番外】第322夜：小狗阿巴想变羊——飞飞姐姐
        "nickname": music_info.get("nickname"),  # 出处作者  喜猫儿和它的小伙伴们
        "album_id": music_info.get("album_id"),  # 专辑id
        "album_title": music_info.get("album_title"),  # 专辑名  睡前故事：一千零一夜
        "category_name": music_info.get("category_name"),  # 音频分类名  ertong
        "category_title": music_info.get("category_title"),  # 音频分类中文名  儿童
        "cover": "",  # 封面名字   自己将内容爬取到本地，然后将名字放入数据库
        "music": "",  # 音频名字
        "intro": music_info.get("intro")  # 音频专辑的简介
    }
    # 自定义下载下来的文件名
    filename = uuid4()

    # 爬取内容到本地，注图片和音频是以字节返回，以res.conternt接收
    cover_url = music_info.get("cover_url")
    music_url = music_info.get("play_path")

    cover = requests.get(cover_url)
    music = requests.get(music_url)

    cover_path = os.path.join(IMAGES_PATH, f'{filename}.jpg')  # 注意发生的目录路劲的坑
    music_path = os.path.join(MUSICS_PATH, f'{filename}.m4a')

    # 将音频的信息保存到mongodb数据库
    music_dict["cover"] = f'{filename}.jpg'
    music_dict["music"] = f'{filename}.m4a'

    DB.contens.insert_one(music_dict)

    # 保存到指定位置
    with open(cover_path, "wb") as f1:
        f1.write(cover.content)

    with open(music_path, "wb") as f2:
        f2.write(music.content)
