# -*- coding:utf-8 -*-
from flask import Blueprint

u"""
声明一个权限管理的Blueprint
"""
auth=Blueprint('auth',__name__)

from . import views