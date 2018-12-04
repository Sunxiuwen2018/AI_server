#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:SunXiuWen
# make_time:2018/12/3
"""用于连接app和玩具连接，app向玩具发送消息，让玩具播放"""
import json
from flask import Flask, request
from geventwebsocket.handler import WebSocketHandler
from gevent.pywsgi import WSGIServer
from geventwebsocket.websocket import WebSocket  # 语法提示

ws_app = Flask(__name__)

socket_dict = {}


@ws_app.route('/app/<app_id>')
def app(app_id):
    """
        逻辑：
        1、建立app的socket连接路由，每次进来都添加到保存所有连接的字典中
        2、app每次连接都带上要和那个玩具通信的id
        3、通过app发的玩具id在socket字典中找到它
        4、将app要发给玩具播放的音频名给它，让它去找服务器获取
    :param app_id:
    :return:
    """
    app_socket = request.environ.get('wsgi.websocket')  # type:WebSocket
    socket_dict[app_id] = app_socket
    print(len(socket_dict), socket_dict)
    while 1:
        # 获取连接发送的消息
        app_msg = app_socket.receive()
        print(app_msg)
        # json格式反序，app发的消息字典
        app_dict = json.loads(app_msg)
        # 获取要联系的玩具id，在app发送消息里有
        tou_user = app_dict.get('to_user')
        # 在所有socket连接中找到app想联系的玩具
        toy_socket = socket_dict.get(tou_user)
        # 将app发的音乐返回给玩具
        toy_socket.send(app_dict.get("music"))


@ws_app.route('/toy/<toy_id>')
def toy(toy_id):
    toy_socket = request.environ.get('wsgi.websocket')  # type:WebSocket
    socket_dict[toy_id] = toy_socket
    print(len(socket_dict), socket_dict)
    while 1:
        toy_msg = toy_socket.receive()
        print("xxxxxx",toy_msg)


if __name__ == '__main__':
    http_serv = WSGIServer(('0.0.0.0', 9527), ws_app, handler_class=WebSocketHandler)
    http_serv.serve_forever()
