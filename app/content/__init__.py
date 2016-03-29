# -*- coding:utf-8 -*-
# -*- coding:utf-8 -*-
from flask import Blueprint

u"""
声明一个内容管理的Blueprint
"""
content=Blueprint('content',__name__)

from . import views