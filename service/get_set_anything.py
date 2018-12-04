#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:SunXiuWen
# make_time:2018/12/1
import os
from flask import Blueprint
from flask import send_file
from settings import (MUSICS_PATH, IMAGES_PATH)

gsa = Blueprint("gsa", __name__)


@gsa.route("/get_image/<filename>")
def get_image(filename):
    """为前端提供视频的图片"""
    image_file = os.path.join(IMAGES_PATH, filename)
    return send_file(image_file)


@gsa.route("/get_music/<filename>")
def get_music(filename):
    music_file = os.path.join(MUSICS_PATH, filename)
    return send_file(music_file)
