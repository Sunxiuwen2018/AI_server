#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:SunXiuWen
# make_time:2018/11/30
from flask import Flask, render_template
from service import contents  # 导入蓝图对象
from service import get_set_anything

app = Flask(__name__)
app.register_blueprint(contents.content)
app.register_blueprint(get_set_anything.gsa)


@app.route('/')
def toy():
    """模拟接收app发给玩具的音频"""
    return render_template('toy.html')


if __name__ == '__main__':
    app.run("0.0.0.0", 9999, debug=True)
