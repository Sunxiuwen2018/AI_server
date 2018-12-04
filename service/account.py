#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:SunXiuWen
# make_time:2018/12/3
from flask import Blueprint
from flask import jsonify, request
from bson import ObjectId
from settings import DB
from settings import RESPONSE_

accounts = Blueprint('accounts', __name__)
